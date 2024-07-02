import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Register from './components/Register';
import Login from './components/Login';
import TripList from './components/TripList';
import Reservation from './components/Reservation';
import Confirmation from './components/Confirmation';
import SecurityToggle from './components/SecurityToggle';

// Créez un thème de base
const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2',
        },
        secondary: {
            main: '#dc004e',
        },
    },
});

function App() {
    return (
        <Router>
            <div className="App">
                <SecurityToggle />
                <Routes>
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/trips" element={<TripList />} />
                    <Route path="/reserve" element={<Reservation />} />
                    <Route path="/confirm" element={<Confirmation />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;