import React, { useState } from 'react';

function Reservation() {
    const [userId, setUserId] = useState('');
    const [tripId, setTripId] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('http://localhost:5000/reserve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: userId, trip_id: tripId })
        });
        const data = await response.json();
        alert(data.message);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Reserve a Trip</h2>
            <div>
                <label>User ID: </label>
                <input 
                    type="text" 
                    value={userId} 
                    onChange={(e) => setUserId(e.target.value)} 
                />
            </div>
            <div>
                <label>Trip ID: </label>
                <input 
                    type="text" 
                    value={tripId} 
                    onChange={(e) => setTripId(e.target.value)} 
                />
            </div>
            <button type="submit">Reserve</button>
        </form>
    );
}

export default Reservation;