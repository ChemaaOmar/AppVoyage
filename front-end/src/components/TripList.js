import React, { useState, useEffect } from 'react';
import { Container, Typography, List, ListItem, ListItemText, Box } from '@mui/material';
import DOMPurify from 'dompurify';

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
        <Container maxWidth="md">
            <Box sx={{ marginTop: 8 }}>
                <Typography variant="h4" component="h2" gutterBottom>
                    Available Trips
                </Typography>
                <List>
                    {trips.map(trip => (
                        <ListItem key={trip.id} sx={{ borderBottom: '1px solid #ccc' }}>
                            <ListItemText 
                                primary={<span dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(`${trip.destination} on ${trip.date}`) }} />}
                                secondary={<span dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(`${trip.available_seats} seats available`) }} />}
                            />
                        </ListItem>
                    ))}
                </List>
            </Box>
        </Container>
    );
}

export default TripList;
