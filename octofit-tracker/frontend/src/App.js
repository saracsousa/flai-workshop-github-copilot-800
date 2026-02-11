import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-5">
      <div className="jumbotron p-5 rounded-3 mb-4">
        <h1 className="display-3 fw-bold">🏋️ Welcome to OctoFit Tracker</h1>
        <p className="lead fs-4">Your fitness journey starts here!</p>
        <hr className="my-4" />
        <p className="fs-5">Track your activities, compete with your team, and reach your fitness goals.</p>
      </div>

      <div className="row g-4">
        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">👥</span>
              </div>
              <h5 className="card-title">Track Users</h5>
              <p className="card-text">Monitor all users and their fitness progress in one place.</p>
              <Link to="/users" className="btn btn-primary">View Users</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">🏆</span>
              </div>
              <h5 className="card-title">Leaderboard</h5>
              <p className="card-text">See who's leading the fitness challenge and get motivated!</p>
              <Link to="/leaderboard" className="btn btn-success">View Rankings</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">💪</span>
              </div>
              <h5 className="card-title">Workouts</h5>
              <p className="card-text">Get personalized workout suggestions based on your goals.</p>
              <Link to="/workouts" className="btn btn-info">Get Workouts</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">👫</span>
              </div>
              <h5 className="card-title">Teams</h5>
              <p className="card-text">Join or create teams and compete together for glory!</p>
              <Link to="/teams" className="btn btn-warning">View Teams</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">📊</span>
              </div>
              <h5 className="card-title">Activities</h5>
              <p className="card-text">Log and view all fitness activities and achievements.</p>
              <Link to="/activities" className="btn btn-danger">View Activities</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="mb-3">
                <span className="display-4">🎯</span>
              </div>
              <h5 className="card-title">Set Goals</h5>
              <p className="card-text">Define your fitness objectives and track your progress.</p>
              <button className="btn btn-secondary" disabled>Coming Soon</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  console.log('OctoFit Tracker App initialized');
  console.log('REACT_APP_CODESPACE_NAME:', process.env.REACT_APP_CODESPACE_NAME);
  console.log('API Base URL: https://' + process.env.REACT_APP_CODESPACE_NAME + '-8000.app.github.dev');

  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-gradient">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <img 
              src="/octofitapp-small.png" 
              alt="OctoFit Logo" 
              className="navbar-logo me-2"
            />
            <span className="fw-bold">OctoFit Tracker</span>
          </Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<Users />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
