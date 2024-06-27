import React, { useState, useEffect } from 'react';

function Confirmation() {
    const [reservations, setReservations] = useState([]);

    useEffect(() => {
        const fetchReservations = async () => {
            const response = await fetch('http://localhost:5000/reservations');
            const data = await response.json();
            setReservations(data);
        };
        fetchReservations();
    }, []);

    return (
        <div>
            <h2>Reservation Confirmations</h2>
            <ul>
                {reservations.map(reservation => (
                    <li key={reservation.id}>
                        Reservation ID: {reservation.id} - User ID: {reservation.user_id} - Trip ID: {reservation.trip_id}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Confirmation;