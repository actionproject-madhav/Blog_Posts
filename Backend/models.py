from pymongo import MongoClient, DESCENDING
from datetime import datetime
from bson import ObjectId
import os

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_database()

# Collections
comments_collection = db.comments
users_collection = db.users

class Comment:
    @staticmethod
    def create(post_slug, content, author_name, author_email=None, 
               author_type='anonymous', google_id=None, parent_id=None):
        """Create a new comment"""
        comment = {
            'post_slug': post_slug,
            'content': content,
            'author_name': author_name,
            'author_email': author_email,
            'author_type': author_type,  # 'anonymous' or 'google'
            'google_id': google_id,
            'parent_id': parent_id,
            'likes': 0,
            'liked_by': [],  # Store IPs or user IDs who liked
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'is_deleted': False,
            'is_approved': True  # Auto-approve, or set False for moderation
        }
        
        result = comments_collection.insert_one(comment)
        comment['_id'] = str(result.inserted_id)
        return comment
    
    @staticmethod
    def get_by_post(post_slug):
        """Get all comments for a post"""
        comments = list(comments_collection.find({
            'post_slug': post_slug,
            'is_deleted': False,
            'is_approved': True
        }).sort('created_at', DESCENDING))
        
        # Convert ObjectId to string
        for comment in comments:
            comment['_id'] = str(comment['_id'])
            if comment.get('parent_id'):
                comment['parent_id'] = str(comment['parent_id'])
        
        # Organize into threads
        return Comment._organize_threads(comments)
    
    @staticmethod
    def _organize_threads(comments):
        """Organize comments into parent-child structure"""
        comment_dict = {c['_id']: c for c in comments}
        root_comments = []
        
        for comment in comments:
            comment['replies'] = []
            
            if comment.get('parent_id'):
                parent = comment_dict.get(comment['parent_id'])
                if parent:
                    parent['replies'].append(comment)
            else:
                root_comments.append(comment)
        
        return root_comments
    
    @staticmethod
    def like(comment_id, user_identifier):
        """Like/unlike a comment"""
        comment = comments_collection.find_one({'_id': ObjectId(comment_id)})
        
        if not comment:
            return None
        
        liked_by = comment.get('liked_by', [])
        
        if user_identifier in liked_by:
            # Unlike
            comments_collection.update_one(
                {'_id': ObjectId(comment_id)},
                {
                    '$inc': {'likes': -1},
                    '$pull': {'liked_by': user_identifier}
                }
            )
            return {'liked': False, 'likes': comment['likes'] - 1}
        else:
            # Like
            comments_collection.update_one(
                {'_id': ObjectId(comment_id)},
                {
                    '$inc': {'likes': 1},
                    '$addToSet': {'liked_by': user_identifier}
                }
            )
            return {'liked': True, 'likes': comment['likes'] + 1}
    
    @staticmethod
    def delete(comment_id):
        """Soft delete a comment"""
        result = comments_collection.update_one(
            {'_id': ObjectId(comment_id)},
            {'$set': {'is_deleted': True, 'updated_at': datetime.utcnow()}}
        )
        return result.modified_count > 0
    
    @staticmethod
    def get_all_for_moderation():
        """Get all comments for admin moderation"""
        comments = list(comments_collection.find({
            'is_deleted': False
        }).sort('created_at', DESCENDING).limit(100))
        
        for comment in comments:
            comment['_id'] = str(comment['_id'])
        
        return comments
    
    @staticmethod
    def approve(comment_id):
        """Approve a comment"""
        result = comments_collection.update_one(
            {'_id': ObjectId(comment_id)},
            {'$set': {'is_approved': True, 'updated_at': datetime.utcnow()}}
        )
        return result.modified_count > 0


class User:
    @staticmethod
    def create_or_get_google_user(google_id, email, name, picture):
        """Create or get a user from Google OAuth"""
        user = users_collection.find_one({'google_id': google_id})
        
        if not user:
            user = {
                'google_id': google_id,
                'email': email,
                'name': name,
                'picture': picture,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow()
            }
            result = users_collection.insert_one(user)
            user['_id'] = str(result.inserted_id)
        else:
            # Update user info
            users_collection.update_one(
                {'google_id': google_id},
                {'$set': {
                    'name': name,
                    'picture': picture,
                    'updated_at': datetime.utcnow()
                }}
            )
            user['_id'] = str(user['_id'])
        
        return user