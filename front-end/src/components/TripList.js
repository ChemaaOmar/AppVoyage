import React, { useState, useEffect } from 'react';

function TripList() {
    const [trips, setTrips] = useState([]);

    useEffect(() => {
        const fetchTrips = async () => {
            const response = await fetch('http://localhost:5000/trips');
            const data = await response.json();
            setTrips(data);
        };
        fetchTrips();
    }, []);

    return (
        <div>
            <h2>Available Trips</h2>
            <ul>
                {trips.map(trip => (
                    <li key={trip.id}>
                        {trip.destination} on {trip.date} - {trip.available_seats} seats available
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TripList;
