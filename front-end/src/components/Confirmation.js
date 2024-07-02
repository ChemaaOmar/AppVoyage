import React, { useState, useEffect } from 'react';
import { Container, Typography, List, ListItem, ListItemText, Box } from '@mui/material';

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
        <Container maxWidth="md">
            <Box sx={{ marginTop: 8 }}>
                <Typography variant="h4" component="h2" gutterBottom>
                    Reservation Confirmations
                </Typography>
                <List>
                    {reservations.map(reservation => (
                        <ListItem key={reservation.id} sx={{ borderBottom: '1px solid #ccc' }}>
                            <ListItemText 
                                primary={`Reservation ID: ${reservation.id}`} 
                                secondary={`User ID: ${reservation.user_id} - Trip ID: ${reservation.trip_id}`} 
                            />
                        </ListItem>
                    ))}
                </List>
            </Box>
        </Container>
    );
}

export default Confirmation;