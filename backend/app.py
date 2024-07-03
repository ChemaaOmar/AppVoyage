from flask import Flask, current_app
from extensions import db, cors, limiter
from config import Config
from flask_limiter.util import get_remote_address
from middleware import apply_security_mode_middleware
from models import SecurityMode

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)
    limiter.init_app(app)  # Initialiser le limiteur avec l'application
    apply_security_mode_middleware(app)

    with app.app_context():
        db.create_all()

        # Initialiser le mode de sécurité dans la base de données si ce n'est pas déjà fait
        if not SecurityMode.query.first():
            secure_mode = SecurityMode(mode='secure')
            db.session.add(secure_mode)
            db.session.commit()

    # Importer et enregistrer les blueprints
    from routes.auth import auth_bp
    from routes.reservations import reservations_bp
    from routes.trips import trips_bp
    from routes.security import security_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(trips_bp)
    app.register_blueprint(security_bp, url_prefix='/security')

    return app

def limit_key_func():
    # Fonction clé pour limiter en fonction du mode de sécurité
    security_mode = SecurityMode.query.first().mode
    if security_mode == 'secure':
        return get_remote_address()
    else:
        return None

@limiter.request_filter
def exempt_unsafe_mode():
    # Exempte les requêtes si le mode est non sécurisé
    security_mode = SecurityMode.query.first().mode
    return security_mode == 'unsafe'

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
