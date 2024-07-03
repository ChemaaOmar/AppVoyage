from flask import Blueprint, jsonify, current_app, make_response
from models import SecurityMode
from extensions import db, csrf
from flask_wtf.csrf import generate_csrf  # Assurez-vous que generate_csrf est importé

security_bp = Blueprint('security', __name__)

@security_bp.route('/get-security-mode', methods=['GET'])
def get_security_mode():
    mode = SecurityMode.query.first().mode
    current_app.logger.info(f'Current security mode: {mode}')
    return jsonify({'mode': mode})

@security_bp.route('/get-csrf-token', methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    response = make_response(jsonify({'csrf_token': csrf_token}))
    response.set_cookie('csrf_token', csrf_token)
    return response

@security_bp.route('/toggle-security', methods=['POST'])
@csrf.exempt
def toggle_security():
    security_mode = SecurityMode.query.first()
    new_mode = 'unsafe' if security_mode.mode == 'secure' else 'secure'
    security_mode.mode = new_mode
    db.session.commit()
    current_app.config['SECURITY_MODE'] = (new_mode == 'secure')
    current_app.logger.info(f'Security mode toggled to: {new_mode}')
    return jsonify({'mode': new_mode})
