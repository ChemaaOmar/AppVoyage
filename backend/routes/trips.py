from flask import Blueprint, jsonify
from models import Trip
from app import db

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/trips', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    result = []
    for trip in trips:
        trip_data = {'id': trip.id, 'destination': trip.destination, 'date': trip.date, 'available_seats': trip.available_seats}
        result.append(trip_data)
    return jsonify(result)
