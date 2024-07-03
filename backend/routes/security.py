from flask import Blueprint, jsonify, current_app
from models import SecurityMode
from extensions import db
from app import limit_key_func, exempt_unsafe_mode  # Importer les fonctions nécessaires

security_bp = Blueprint('security', __name__)

@security_bp.route('/get-security-mode', methods=['GET'])
def get_security_mode():
    mode = SecurityMode.query.first().mode
    current_app.logger.info(f'Current security mode: {mode}')  # Message de journalisation
    return jsonify({'mode': mode})

@security_bp.route('/toggle-security', methods=['POST'])
def toggle_security():
    security_mode = SecurityMode.query.first()
    new_mode = 'unsafe' if security_mode.mode == 'secure' else 'secure'
    security_mode.mode = new_mode
    db.session.commit()
    current_app.config['SECURITY_MODE'] = (new_mode == 'secure')
    
    current_app.logger.info(f'Security mode toggled to: {new_mode}')  # Message de journalisation
    
    return jsonify({'mode': new_mode})
