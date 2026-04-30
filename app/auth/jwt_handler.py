import jwt
import datetime
from flask import request, jsonify

SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key

# Function to create a JWT token
def create_token(user_id, role):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    token = jwt.encode({'user_id': user_id, 'role': role, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
    return token

# Function to verify a JWT token
def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Function for role-based access control
def role_required(required_role):
    def wrapper(f):
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization').split(" ")[1]
            decoded = verify_token(token)

            if not decoded or decoded['role'] != required_role:
                return jsonify({'message': 'Unauthorized'}), 403

            return f(*args, **kwargs)
        return decorated
    return wrapper

# Example usage:
# @app.route('/protected', methods=['GET'])
# @role_required('admin')
# def protected_route():
#     return jsonify({'message': 'This is a protected route'}).
