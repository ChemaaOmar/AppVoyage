from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_limiter.errors import RateLimitExceeded
import bleach

auth_bp = Blueprint('auth', __name__)
limiter = Limiter(key_func=get_remote_address)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = bleach.clean(data['username'])
    password = bleach.clean(data['password'])
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = bleach.clean(data['username'])
        password = bleach.clean(data['password'])
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Login failed'}), 401
        return jsonify({'message': 'Logged in successfully'})
    except RateLimitExceeded:
        return jsonify({'message': 'Too many login attempts. Please try again later.'}), 429

# Définir le décorateur conditionnellement en fonction du mode de sécurité
def conditional_login():
    if current_app.config['SECURITY_MODE']:
        return limiter.limit("5 per minute")(login)()
    else:
        return login()

# Ajouter la route avec le décorateur conditionnellement
auth_bp.add_url_rule('/login', 'conditional_login', conditional_login, methods=['POST'])
