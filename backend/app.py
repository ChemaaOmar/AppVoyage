from flask import Flask
from extensions import db, cors
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)

    print(f"SQLAlchemy instance in app: {db}")  # Ajout d'un point de contrôle

    # Importer et enregistrer les blueprints
    from routes.auth import auth_bp
    from routes.reservations import reservations_bp
    from routes.trips import trips_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(trips_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
