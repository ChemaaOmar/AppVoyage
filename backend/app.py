from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object('config.Config')
db = SQLAlchemy(app)

# Importer les blueprints à la fin pour éviter les imports circulaires
def create_app():
    from routes.auth import auth_bp
    from routes.reservations import reservations_bp
    from routes.trips import trips_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(trips_bp)

    return app

if __name__ == '__main__':
    create_app()
    app.run(debug=True)
