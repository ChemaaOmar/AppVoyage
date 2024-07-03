from flask import Flask
from extensions import db, cors
from config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)
    
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["240 per day", "10 per hour"]
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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
