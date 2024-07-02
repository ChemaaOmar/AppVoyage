from flask import Blueprint, jsonify, current_app
from models import Trip
from extensions import db
from sqlalchemy import text

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/trips', methods=['GET'])
def get_trips():
    if current_app.config['SECURITY_MODE']:
        # Mode sécurisé : utiliser SQLAlchemy avec des requêtes sécurisées
        trips = Trip.query.all()
    else:
        # Mode non sécurisé : exécuter une requête brute (vulnérable à l'injection SQL)
        result = db.session.execute(text('SELECT * FROM trip'))
        trips = [Trip(id=row[0], destination=row[1], date=row[2], available_seats=row[3]) for row in result]
    
    result = []
    for trip in trips:
        trip_data = {'id': trip.id, 'destination': trip.destination, 'date': trip.date, 'available_seats': trip.available_seats}
        result.append(trip_data)
    return jsonify(result)

@trips_bp.route('/trips/<destination>', methods=['GET'])
def get_trips_by_destination(destination):
    if current_app.config['SECURITY_MODE']:
        # Mode sécurisé : utiliser SQLAlchemy avec des requêtes sécurisées
        trips = Trip.query.filter_by(destination=destination).all()
    else:
        # Mode non sécurisé : exécuter une requête brute (vulnérable à l'injection SQL)
        result = db.session.execute(text(f"SELECT * FROM trip WHERE destination = '{destination}'"))
        trips = [Trip(id=row[0], destination=row[1], date=row[2], available_seats=row[3]) for row in result]
    
    result = []
    for trip in trips:
        trip_data = {'id': trip.id, 'destination': trip.destination, 'date': trip.date, 'available_seats': trip.available_seats}
        result.append(trip_data)
    return jsonify(result)
