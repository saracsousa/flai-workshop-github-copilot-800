import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedWorkout, setSelectedWorkout] = useState(null);

  const handleStartWorkout = (workout) => {
    setSelectedWorkout(workout);
    alert(`🚀 Starting workout: ${workout.name}\n\nDuration: ${workout.duration} min\nDifficulty: ${workout.difficulty}\nPoints: ${workout.points}\n\nGood luck! 💪`);
  };

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching workouts from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        console.log('Workouts API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Raw workouts data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="text-center">
          <div className="spinner-border text-info loading-spinner" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3 fs-5">Loading workouts...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger d-flex align-items-center" role="alert">
          <span className="me-2">⚠️</span>
          <div>
            <strong>Error:</strong> {error}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="page-header mb-4">
        <h2 className="mb-0">💪 Workout Suggestions</h2>
        <p className="mb-0 mt-2 opacity-75">Get personalized workout suggestions to reach your fitness goals</p>
      </div>

      <div className="row g-4">
        {workouts.length === 0 ? (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <h4 className="alert-heading">No Workouts Available</h4>
              <p className="mb-0">No workout suggestions found. Check back later!</p>
            </div>
          </div>
        ) : (
          workouts.map((workout, index) => (
            <div className="col-md-6 col-lg-4" key={workout.id || index}>
              <div className="card h-100 shadow-sm">
                <div className="card-header">
                  <h5 className="mb-0">{workout.name}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text text-muted">{workout.description}</p>
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Type:</strong></span>
                      <span className="badge bg-info">{workout.workout_type}</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Duration:</strong></span>
                      <span className="badge bg-success">{workout.duration} min</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Difficulty:</strong></span>
                      <span className={`badge ${
                        workout.difficulty === 'Easy' ? 'bg-success' :
                        workout.difficulty === 'Medium' ? 'bg-warning' :
                        'bg-danger'
                      }`}>
                        {workout.difficulty}
                      </span>
                    </li>
                    {workout.equipment && (
                      <li className="list-group-item d-flex justify-content-between align-items-center">
                        <span><strong>Equipment:</strong></span>
                        <span className="badge bg-secondary">{workout.equipment}</span>
                      </li>
                    )}
                  </ul>
                </div>
                <div className="card-footer">
                  <button 
                    className="btn btn-primary w-100" 
                    onClick={() => handleStartWorkout(workout)}
                  >
                    🚀 Start Workout
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {workouts.length > 0 && (
        <div className="mt-4 text-center">
          <p className="text-muted">Total Workouts: {workouts.length}</p>
        </div>
      )}
    </div>
  );
}

export default Workouts;
