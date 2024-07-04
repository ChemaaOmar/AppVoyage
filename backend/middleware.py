from flask import request, current_app
from flask_wtf.csrf import CSRFProtect, generate_csrf
from models import SecurityMode
import logging

csrf = CSRFProtect()

def apply_security_mode_middleware(app):
    @app.before_request
    def check_security_mode():
        security_mode = SecurityMode.query.first().mode
        current_app.logger.debug(f'Current security mode: {security_mode}')
        if security_mode == 'unsafe':
            csrf.exempt('routes.security.toggle_security')
            current_app.logger.debug('CSRF protection exempted for /toggle-security')
        else:
            csrf._exempt_views.clear()
            current_app.logger.debug('CSRF protection applied for /toggle-security')

    @app.after_request
    def set_csrf_token(response):
        if request.method == "GET" and 'csrf_token' not in request.cookies:
            csrf_token = generate_csrf()
            response.set_cookie('csrf_token', csrf_token)
        return response

    csrf.init_app(app)
