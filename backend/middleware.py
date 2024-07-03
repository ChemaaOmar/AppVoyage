from flask import request, current_app
from flask_wtf.csrf import CSRFProtect, generate_csrf
from models import SecurityMode

csrf = CSRFProtect()

def apply_security_mode_middleware(app):
    @app.before_request
    def check_security_mode():
        security_mode = SecurityMode.query.first().mode
        if security_mode == 'unsafe':
            csrf._exempt_views.add('*')
        else:
            csrf._exempt_views.clear()

    @app.after_request
    def set_csrf_token(response):
        if request.method == "GET" and 'csrf_token' not in request.cookies:
            csrf_token = generate_csrf()
            response.set_cookie('csrf_token', csrf_token)
        return response

    csrf.init_app(app)
