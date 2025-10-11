from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

app = Flask(__name__)
CORS(app, origins=os.getenv('ALLOWED_ORIGINS', 'http://localhost:5173').split(','))

# MongoDB connection with proper URI handling
def get_mongo_client():
    """Get MongoDB client with proper URI encoding"""
    mongodb_uri = os.getenv('MONGODB_URI')
    if not mongodb_uri:
        raise ValueError("MONGODB_URI environment variable not set")
    
    try:
        # Try to connect with the URI as-is first
        return MongoClient(mongodb_uri)
    except Exception as e:
        if "InvalidURI" in str(e) and "quote_plus" in str(e):
            print("Warning: MongoDB URI contains special characters that need encoding")
            print("Please URL-encode your username and password in the MONGODB_URI")
            print("Example: password 'my@password' should be 'my%40password'")
        raise e

try:
    client = get_mongo_client()
    db = client.get_database()
    comments = db.comments
    print("✅ Connected to MongoDB successfully")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    print("\nTo fix this:")
    print("1. Create a .env file in the Backend directory")
    print("2. Add your MongoDB URI with URL-encoded credentials")
    print("3. Example: MONGODB_URI=mongodb+srv://username:encoded_password@cluster.mongodb.net/db")
    client = None
    db = None
    comments = None


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


@app.route('/api/comments/<post_slug>', methods=['GET'])
def get_comments(post_slug):
    """Get all comments for a post"""
    if not comments:
        return jsonify({'success': False, 'error': 'Database not connected'}), 500
    
    try:
        comment_list = list(comments.find({
            'post_slug': post_slug,
            'is_deleted': False
        }).sort('created_at', -1))
        
        # Convert ObjectId to string
        for comment in comment_list:
            comment['_id'] = str(comment['_id'])
        
        return jsonify({
            'success': True,
            'comments': comment_list
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/comments', methods=['POST'])
def create_comment():
    """Create a new comment"""
    if not comments:
        return jsonify({'success': False, 'error': 'Database not connected'}), 500
    
    try:
        data = request.get_json()
        
        # Get data
        post_slug = data.get('post_slug', '').strip()
        author_name = data.get('author_name', '').strip()
        content = data.get('content', '').strip()
        
        # Validate
        if not post_slug or not author_name or not content:
            return jsonify({
                'success': False,
                'error': 'All fields required'
            }), 400
        
        if len(content) < 3:
            return jsonify({
                'success': False,
                'error': 'Comment too short'
            }), 400
        
        if len(content) > 1000:
            return jsonify({
                'success': False,
                'error': 'Comment too long (max 1000 characters)'
            }), 400
        
        # Create comment
        comment = {
            'post_slug': post_slug,
            'author_name': author_name,
            'content': content,
            'created_at': datetime.utcnow(),
            'is_deleted': False
        }
        
        result = comments.insert_one(comment)
        comment['_id'] = str(result.inserted_id)
        
        return jsonify({
            'success': True,
            'comment': comment
        }), 201
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)