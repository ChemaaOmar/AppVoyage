import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import TripList from './components/TripList';
import Reservation from './components/Reservation';
import Confirmation from './components/Confirmation';

function App() {
    return (
        <Router>
            <div className="App">
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
