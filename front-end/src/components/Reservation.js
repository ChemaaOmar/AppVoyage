import React, { useState } from 'react';
import { TextField, Button, Typography, Container, Box } from '@mui/material';

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
        <Container maxWidth="xs">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Typography component="h1" variant="h5">
                    Reserve a Trip
                </Typography>
                <Box component="form" onSubmit={handleSubmit} sx={{ mt: 1 }}>
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="userId"
                        label="User ID"
                        name="userId"
                        autoComplete="userId"
                        autoFocus
                        value={userId}
                        onChange={(e) => setUserId(e.target.value)}
                    />
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="tripId"
                        label="Trip ID"
                        name="tripId"
                        autoComplete="tripId"
                        value={tripId}
                        onChange={(e) => setTripId(e.target.value)}
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Reserve
                    </Button>
                </Box>
            </Box>
        </Container>
    );
}

export default Reservation;
