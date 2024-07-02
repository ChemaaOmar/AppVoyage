from flask import Blueprint, request, jsonify, current_app
from models import Reservation
from extensions import db
from sqlalchemy import text

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reserve', methods=['POST'])
def reserve():
    data = request.get_json()
    user_id = data['user_id']
    trip_id = data['trip_id']

    if current_app.config['SECURITY_MODE']:
        # Mode sécurisé : utiliser SQLAlchemy avec des requêtes sécurisées
        new_reservation = Reservation(user_id=user_id, trip_id=trip_id)
        db.session.add(new_reservation)
        db.session.commit()
    else:
        # Mode non sécurisé : exécuter une requête brute (vulnérable à l'injection SQL)
        db.session.execute(text(f"INSERT INTO reservation (user_id, trip_id) VALUES ({user_id}, {trip_id})"))
    
    return jsonify({'message': 'Reservation successful'})
