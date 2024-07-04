from flask import Flask
from extensions import db, cors, limiter, csrf
from config import Config
from middleware import apply_security_mode_middleware
from models import SecurityMode

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'your_secret_key'

    cors.init_app(app, resources={r"*": {"origins": "http://localhost:3000"}})
    db.init_app(app)
    limiter.init_app(app)
    
    apply_security_mode_middleware(app)

    with app.app_context():
        db.create_all()

        if not SecurityMode.query.first():
            secure_mode = SecurityMode(mode='secure')
            db.session.add(secure_mode)
            db.session.commit()

    from routes.auth import auth_bp
    from routes.reservations import reservations_bp
    from routes.trips import trips_bp
    from routes.security import security_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(trips_bp)
    app.register_blueprint(security_bp, url_prefix='/security')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
