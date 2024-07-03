from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

auth_bp = Blueprint('auth', __name__)
limiter = Limiter(key_func=get_remote_address)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    if current_app.config['SECURITY_MODE']:
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    else:
        hashed_password = password  # Stocker en clair en mode non sécurisé

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registered successfully'})

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Limite à 5 tentatives par minute
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'message': 'Login failed'}), 401

    if current_app.config['SECURITY_MODE']:
        if not check_password_hash(user.password, password):
            return jsonify({'message': 'Login failed'}), 401
    else:
        if user.password != password:
            return jsonify({'message': 'Login failed'}), 401
    
    return jsonify({'message': 'Logged in successfully', 'password': user.password})  # Envoie le mot de passe en clair en mode non sécurisé
