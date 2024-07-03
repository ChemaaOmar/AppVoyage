from flask import request, current_app
from models import SecurityMode
from extensions import db

def apply_security_mode_middleware(app):
    @app.before_request
    def check_security_mode():
        security_mode = SecurityMode.query.first().mode
        current_app.config['SECURITY_MODE'] = (security_mode == 'secure')
