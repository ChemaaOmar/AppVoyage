from flask import Blueprint, jsonify, current_app
from models import SecurityMode
from extensions import db

security_bp = Blueprint('security', __name__)

@security_bp.route('/get-security-mode', methods=['GET'])
def get_security_mode():
    mode = SecurityMode.query.first().mode
    return jsonify({'mode': mode})

@security_bp.route('/toggle-security', methods=['POST'])
def toggle_security():
    security_mode = SecurityMode.query.first()
    new_mode = 'unsafe' if security_mode.mode == 'secure' else 'secure'
    security_mode.mode = new_mode
    db.session.commit()
    current_app.config['SECURITY_MODE'] = (new_mode == 'secure')
    return jsonify({'mode': new_mode})
