from flask import Blueprint, request, jsonify
from extensions import db
from models import Trip
import bleach

trips_bp = Blueprint('trips', __name__)

# Route pour obtenir tous les voyages
@trips_bp.route('/trips', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    return jsonify([{
        'id': trip.id,
        'destination': bleach.clean(trip.destination),
        'date': bleach.clean(trip.date),
        'available_seats': trip.available_seats
    } for trip in trips])

# Route pour ajouter un nouveau voyage
@trips_bp.route('/trips', methods=['POST'])
def add_trip():
    data = request.get_json()
    # Nettoyage des entrées utilisateur
    destination = bleach.clean(data.get('destination'))
    date = bleach.clean(data.get('date'))
    available_seats = data.get('available_seats')

    new_trip = Trip(destination=destination, date=date, available_seats=available_seats)
    db.session.add(new_trip)
    db.session.commit()
    return jsonify({'message': 'Trip added successfully'})
