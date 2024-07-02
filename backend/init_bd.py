from app import create_app, db
from models import User, Trip
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()

    # Ajout de quelques utilisateurs et voyages pour les tests
    user1 = User(username='testuser1', password=generate_password_hash('password1'))
    user2 = User(username='testuser2', password=generate_password_hash('password2'))
    trip1 = Trip(destination='Paris', date='2024-07-20', available_seats=10)
    trip2 = Trip(destination='New York', date='2024-08-15', available_seats=5)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(trip1)
    db.session.add(trip2)
    db.session.commit()
