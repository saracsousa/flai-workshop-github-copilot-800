import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Fetching leaderboard from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        console.log('Leaderboard API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Raw leaderboard data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="text-center">
          <div className="spinner-border text-warning loading-spinner" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3 fs-5">Loading leaderboard...</p>
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
        <h2 className="mb-0">🏆 Leaderboard</h2>
        <p className="mb-0 mt-2 opacity-75">See who's leading the fitness challenge</p>
      </div>

      <div className="card">
        <div className="card-body p-0">
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead>
                <tr>
                  <th scope="col" className="text-center" style={{width: '80px'}}>Rank</th>
                  <th scope="col">User</th>
                  <th scope="col">Team</th>
                  <th scope="col" className="text-center">Total Points</th>
                  <th scope="col" className="text-center">Activities</th>
                </tr>
              </thead>
              <tbody>
                {leaderboard.length === 0 ? (
                  <tr>
                    <td colSpan="5" className="text-center py-4">
                      <span className="text-muted">No leaderboard data found</span>
                    </td>
                  </tr>
                ) : (
                  leaderboard.map((entry, index) => {
                    const rank = entry.rank || index + 1;
                    let rankBadge = 'bg-secondary';
                    let medal = '';
                    if (rank === 1) {
                      rankBadge = 'bg-warning';
                      medal = '🥇';
                    } else if (rank === 2) {
                      rankBadge = 'bg-secondary';
                      medal = '🥈';
                    } else if (rank === 3) {
                      rankBadge = 'bg-danger';
                      medal = '🥉';
                    }
                    
                    return (
                      <tr key={entry.id || index}>
                        <td className="text-center">
                          <span className={`badge ${rankBadge} fs-6`}>
                            {medal} {rank}
                          </span>
                        </td>
                        <td className="fw-bold">{entry.user}</td>
                        <td><span className="badge bg-primary">{entry.team}</span></td>
                        <td className="text-center">
                          <strong className="text-success fs-5">{entry.total_points}</strong>
                        </td>
                        <td className="text-center">{entry.activity_count}</td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
        <div className="card-footer text-muted">
          Total Participants: {leaderboard.length}
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
