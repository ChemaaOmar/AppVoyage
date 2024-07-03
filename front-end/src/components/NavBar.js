import React, { useContext, useState, useEffect } from 'react';
import { AppBar, Toolbar, Typography, Box, Button } from '@mui/material';
import { useNavigate, useLocation } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import Switch from 'react-switch';

function NavBar() {
    const { logout, isAuthenticated } = useContext(AuthContext);
    const navigate = useNavigate();
    const location = useLocation();
    const [mode, setMode] = useState('secure');

    useEffect(() => {
        const fetchSecurityMode = async () => {
            const response = await fetch('http://localhost:5000/security/get-security-mode');
            const data = await response.json();
            setMode(data.mode);
        };
        fetchSecurityMode();
    }, []);

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    const toggleSecurity = async () => {
        const response = await fetch('http://localhost:5000/security/toggle-security', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        setMode(data.mode);
    };

    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    Travel Booking App
                </Typography>
                <Box display="flex" alignItems="center">
                    <Typography variant="body1" component="div" sx={{ mr: 2 }}>
                        {mode === 'secure' ? 'Secure Mode' : 'Insecure Mode'}
                    </Typography>
                    <Switch
                        checked={mode === 'secure'}
                        onChange={toggleSecurity}
                        offColor="#FF0000"
                        onColor="#00FF00"
                        uncheckedIcon={false}
                        checkedIcon={false}
                        handleDiameter={20}
                        height={24}
                        width={48}
                    />
                    {isAuthenticated && (
                        <Button color="inherit" onClick={handleLogout} sx={{ ml: 2 }}>
                            Logout
                        </Button>
                    )}
                </Box>
            </Toolbar>
        </AppBar>
    );
}

export default NavBar;
