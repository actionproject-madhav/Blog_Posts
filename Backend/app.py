from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from models import Comment, User
from auth import requires_admin_auth
from config import Config
import re
from email_validator import validate_email, EmailNotValidError
from google.oauth2 import id_token
from google.auth.transport import requests

app = Flask(__name__)
app.config.from_object(Config)

# CORS
CORS(app, origins=Config.ALLOWED_ORIGINS, supports_credentials=True)

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=Config.RATELIMIT_STORAGE_URL
)

# Helper functions
def sanitize_input(text):
    """Remove HTML tags and excessive whitespace"""
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_user_identifier():
    """Get a unique identifier for the user (IP or session)"""
    return request.headers.get('X-Forwarded-For', request.remote_addr)

# Routes
@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/comments/<post_slug>', methods=['GET'])
def get_comments(post_slug):
    """Get all comments for a post"""
    try:
        comments = Comment.get_by_post(post_slug)
        return jsonify({
            'success': True,
            'comments': comments,
            'count': len(comments)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/comments', methods=['POST'])
@limiter.limit("10 per hour")
def create_comment():
    """Create a new comment"""
    try:
        data = request.get_json()
        
        # Required fields
        post_slug = data.get('post_slug')
        content = data.get('content')
        author_name = data.get('author_name')
        
        if not all([post_slug, content, author_name]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400
        
        # Sanitize inputs
        post_slug = sanitize_input(post_slug)
        content = sanitize_input(content)
        author_name = sanitize_input(author_name)
        
        # Validate content length
        if len(content) < 3:
            return jsonify({
                'success': False,
                'error': 'Comment too short (minimum 3 characters)'
            }), 400
        
        if len(content) > 2000:
            return jsonify({
                'success': False,
                'error': 'Comment too long (maximum 2000 characters)'
            }), 400
        
        # Validate author name
        if len(author_name) < 2 or len(author_name) > 50:
            return jsonify({
                'success': False,
                'error': 'Name must be between 2 and 50 characters'
            }), 400
        
        # Handle email (optional)
        author_email = data.get('author_email')
        if author_email:
            author_email = author_email.strip().lower()
            try:
                validate_email(author_email)
            except EmailNotValidError:
                return jsonify({
                    'success': False,
                    'error': 'Invalid email address'
                }), 400
        
        # Handle Google OAuth token (optional)
        google_token = data.get('google_token')
        google_id = None
        author_type = 'anonymous'
        
        if google_token:
            try:
                idinfo = id_token.verify_oauth2_token(
                    google_token, 
                    requests.Request(), 
                    Config.GOOGLE_CLIENT_ID
                )
                google_id = idinfo['sub']
                author_name = idinfo.get('name', author_name)
                author_email = idinfo.get('email', author_email)
                author_type = 'google'
                
                # Create or update user
                User.create_or_get_google_user(
                    google_id, 
                    author_email, 
                    author_name,
                    idinfo.get('picture')
                )
            except ValueError:
                # Invalid token, continue as anonymous
                pass
        
        # Parent comment ID (for replies)
        parent_id = data.get('parent_id')
        
        # Create comment
        comment = Comment.create(
            post_slug=post_slug,
            content=content,
            author_name=author_name,
            author_email=author_email,
            author_type=author_type,
            google_id=google_id,
            parent_id=parent_id
        )
        
        return jsonify({
            'success': True,
            'message': 'Comment posted successfully',
            'comment': comment
        }), 201
    
    except Exception as e:
        print(f"Error creating comment: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/comments/<comment_id>/like', methods=['POST'])
@limiter.limit("30 per minute")
def like_comment(comment_id):
    """Like/unlike a comment"""
    try:
        user_identifier = get_user_identifier()
        result = Comment.like(comment_id, user_identifier)
        
        if result is None:
            return jsonify({
                'success': False,
                'error': 'Comment not found'
            }), 404
        
        return jsonify({
            'success': True,
            'liked': result['liked'],
            'likes': result['likes']
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Admin routes
@app.route('/api/admin/comments', methods=['GET'])
@requires_admin_auth
def get_all_comments():
    """Get all comments for moderation"""
    try:
        comments = Comment.get_all_for_moderation()
        return jsonify({
            'success': True,
            'comments': comments
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/admin/comments/<comment_id>/approve', methods=['POST'])
@requires_admin_auth
def approve_comment(comment_id):
    """Approve a comment"""
    try:
        success = Comment.approve(comment_id)
        if success:
            return jsonify({
                'success': True,
                'message': 'Comment approved'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Comment not found'
            }), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/admin/comments/<comment_id>', methods=['DELETE'])
@requires_admin_auth
def delete_comment(comment_id):
    """Delete a comment"""
    try:
        success = Comment.delete(comment_id)
        if success:
            return jsonify({
                'success': True,
                'message': 'Comment deleted'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Comment not found'
            }), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)