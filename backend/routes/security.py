from flask import Blueprint, jsonify, current_app

security_bp = Blueprint('security', __name__)

@security_bp.route('/toggle-security', methods=['POST'])
def toggle_security():
    current_app.config['SECURITY_MODE'] = not current_app.config['SECURITY_MODE']
    mode = 'secure' if current_app.config['SECURITY_MODE'] else 'insecure'
    return jsonify({'message': f'Security mode switched to {mode}', 'mode': mode})

@security_bp.route('/get-security-mode', methods=['GET'])
def get_security_mode():
    mode = 'secure' if current_app.config['SECURITY_MODE'] else 'insecure'
    return jsonify({'mode': mode})
