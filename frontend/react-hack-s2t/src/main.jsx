import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
import Welcome from './welcome';
import Teeth from './teeth';
import TeethInput from './teethInput';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/app" element={<App />} />
        <Route path="/teeth" element={<Teeth />} />
        <Route path="/TeethInput" element={<TeethInput />} />
      </Routes>
    </Router>
  </React.StrictMode>
);