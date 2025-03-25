import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem('token', data.access_token); // Store JWT in localStorage
        localStorage.setItem('user', JSON.stringify(data.user)); // Store user details
        navigate('/App'); // Redirect to another page
      } else {
        setError(data.error || 'Credenziali errate');
      }
    } catch (err) {
      setError('Errore di connessione');
    }
  };

  return (
    <div className='overlay'>
      <div className="login-container">
        <form onSubmit={handleLogin} className="login-form">
          <h1>Login</h1>
          {error && <div className="error-message">{error}</div>}
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              placeholder="Inserisci il tuo username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              placeholder="Inserisci la tua password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="login-button">Login</button>
          <p className="register-link">
            Non hai un account? <Link to="/register">Registrati</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;
