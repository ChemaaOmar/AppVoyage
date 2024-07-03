from flask import Flask
from extensions import db, cors
from config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from middleware import apply_security_mode_middleware

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)
    apply_security_mode_middleware(app)
    
    with app.app_context():
        db.create_all()
        
        # Initialiser le mode de sécurité dans la base de données si ce n'est pas déjà fait
        from models import SecurityMode
        if not SecurityMode.query.first():
            secure_mode = SecurityMode(mode='secure')
            db.session.add(secure_mode)
            db.session.commit()
    
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["200 per day", "5 per hour"] if app.config['SECURITY_MODE'] else []
    )

    # Importer et enregistrer les blueprints
    from routes.auth import auth_bp
    from routes.reservations import reservations_bp
    from routes.trips import trips_bp
    from routes.security import security_bp

    app.register_blueprint(auth_bp)  # Sans le préfixe '/auth'
    app.register_blueprint(reservations_bp)
    app.register_blueprint(trips_bp)
    app.register_blueprint(security_bp, url_prefix='/security')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
