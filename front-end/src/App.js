import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Register from './components/Register';
import Login from './components/Login';
import TripList from './components/TripList';
import Reservation from './components/Reservation';
import Confirmation from './components/Confirmation';
import { AuthProvider } from './context/AuthContext';
import NavBar from './components/NavBar';

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
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <AuthProvider>
                    <NavBar />
                    <div className="App">
                        <Routes>
                            <Route path="/register" element={<Register />} />
                            <Route path="/login" element={<Login />} />
                            <Route path="/trips" element={<TripList />} />
                            <Route path="/reserve" element={<Reservation />} />
                            <Route path="/confirm" element={<Confirmation />} />
                        </Routes>
                    </div>
                </AuthProvider>
            </Router>
        </ThemeProvider>
    );
}

export default App;
