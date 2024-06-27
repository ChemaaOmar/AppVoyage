from flask import Blueprint, request, jsonify
from app import db
from models import Reservation

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reserve', methods=['POST'])
def reserve():
    data = request.get_json()
    new_reservation = Reservation(user_id=data['user_id'], trip_id=data['trip_id'])
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation successful'})
