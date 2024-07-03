from flask import Blueprint, request, jsonify
from extensions import db
from models import Reservation
import bleach

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reserve', methods=['POST'])
def reserve_trip():
    data = request.get_json()
    user_id = bleach.clean(data.get('user_id'))
    trip_id = bleach.clean(data.get('trip_id'))

    new_reservation = Reservation(user_id=user_id, trip_id=trip_id)
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation successful'})

@reservations_bp.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{
        'id': reservation.id,
        'user_id': bleach.clean(reservation.user_id),
        'trip_id': reservation.trip_id
    } for reservation in reservations])
