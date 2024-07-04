from flask import Blueprint, request, jsonify, current_app
from extensions import db, limiter
from models import User
from utils import limit_key_func  # Assurez-vous que cette importation est correcte

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute", key_func=limit_key_func)
def login():
    try:
        data = request.get_json()
        current_app.logger.debug(f'Login data received: {data}')

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            current_app.logger.info(f'User {username} logged in successfully')
            return jsonify({'message': 'Login successful'}), 200
        else:
            current_app.logger.warning(f'Login failed for user {username}')
            return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        current_app.logger.error(f'Error during login: {e}')
        return jsonify({'error': 'Bad request'}), 400

@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per minute", key_func=limit_key_func)
def register():
    try:
        data = request.get_json()
        current_app.logger.debug(f'Registration data received: {data}')

        username = data.get('username')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            current_app.logger.warning(f'Username {username} is already taken')
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        current_app.logger.info(f'User {username} registered successfully')
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        current_app.logger.error(f'Error during registration: {e}')
        return jsonify({'error': 'Bad request'}), 400
