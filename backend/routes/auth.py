from flask import Blueprint, request, jsonify
from extensions import db, limiter
from models import User
from app import limit_key_func  # Importer limit_key_func
import bleach

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per minute", key_func=limit_key_func)
def register():
    data = request.get_json()
    username = bleach.clean(data.get('username'))
    password = bleach.clean(data.get('password'))
    if not username or not password:
        return jsonify({"message": "Invalid input"}), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute", key_func=limit_key_func)
def login():
    data = request.get_json()
    username = bleach.clean(data.get('username'))
    password = bleach.clean(data.get('password'))
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401
