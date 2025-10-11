from functools import wraps
from flask import request, jsonify
import bcrypt
from config import Config

def check_admin_auth(username, password):
    """Check if admin credentials are valid"""
    return (username == Config.ADMIN_USERNAME and 
            password == Config.ADMIN_PASSWORD)

def requires_admin_auth(f):
    """Decorator for admin-only endpoints"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_admin_auth(auth.username, auth.password):
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        return f(*args, **kwargs)
    return decorated