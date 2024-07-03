import React, { useState } from 'react';
import { Container, Typography, TextField, Button, Box } from '@mui/material';
import DOMPurify from 'dompurify';

function Reservation() {
    const [userId, setUserId] = useState('');
    const [tripId, setTripId] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/reserve', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_id: userId, trip_id: tripId }),
            });

            const data = await response.json();
            if (response.ok) {
                setMessage(data.message);
            } else {
                setMessage(data.message || 'Reservation failed');
            }
        } catch (error) {
            setMessage('Failed to connect to the server');
        }
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
                <Typography variant="h4" component="h1" gutterBottom>
                    Reserve a Trip
                </Typography>
                {message && (
                    <Typography variant="body1" color="error" gutterBottom>
                        <span dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(message) }} />
                    </Typography>
                )}
                <form onSubmit={handleSubmit}>
                    <TextField
                        label="User ID"
                        variant="outlined"
                        margin="normal"
                        fullWidth
                        value={userId}
                        onChange={(e) => setUserId(e.target.value)}
                    />
                    <TextField
                        label="Trip ID"
                        variant="outlined"
                        margin="normal"
                        fullWidth
                        value={tripId}
                        onChange={(e) => setTripId(e.target.value)}
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        fullWidth
                        sx={{ mt: 2 }}
                    >
                        Reserve
                    </Button>
                </form>
            </Box>
        </Container>
    );
}

export default Reservation;
