import React, { useState } from 'react';
import '../css/login.css';
import { Link } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    // Qui puoi aggiungere la logica per il login
    console.log('Username:', username);
    console.log('Password:', password);
  };

  return (
    <div className='overlay'>
    <div className="login-container">
      <form onSubmit={handleLogin} className="login-form">
        <h1>Login</h1>
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            placeholder='Inserisci il tuo username'
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
            placeholder='Inserisci la tua password'
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