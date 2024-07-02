from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        # Créer toutes les tables
        db.create_all()

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
    app.run(debug=True)
