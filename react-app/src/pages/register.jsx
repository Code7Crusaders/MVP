// src/Register.js
import React, { useState } from 'react';
import '../css/register.css';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    confirmPassword: '',
    email: '',
    phone: '',
    firstName: '',
    lastName: ''
  });

  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    
    const { name, value } = e.target;
    
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
  
    if (formData.password !== formData.confirmPassword) {
      setError('Le password non coincidono');
      return;
    }
  
    if (formData.phone && formData.phone.length !== 16) {
      setError('Il numero di telefono deve avere 16 caratteri');
      return;
    }
  
    try {
      const response = await fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: formData.username,
          password: formData.password,
          email: formData.email,
          phone: formData.phone,
          first_name: formData.firstName,
          last_name: formData.lastName,
        }),
      });
  
      const data = await response.json();
  
      if (response.ok) {
        navigate('/login');
      } else {
        setError(data.error || 'Registrazione fallita');
      }
    } catch (err) {
      setError('Errore di connessione');
    }
  };
  

  return (
    <div className="register-container">
      <form onSubmit={handleSubmit} className="register-form">
  <h1>Registrazione</h1>
  {error && <div className="error-message">{error}</div>}

  <div className="form-container">
    {/* Sezione Sinistra */}
    <div className="left-section">
      <div className="form-group">
        <label>Username*</label>
        <input
          type="text"
          name="username"
          value={formData.username}
          placeholder="Inserisci il tuo username"
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Email*</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          placeholder="Inserisci la tua email"
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Nome*</label>
        <input
          type="text"
          name="firstName"
          value={formData.firstName}
          placeholder="Inserisci il tuo nome"
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Cognome*</label>
        <input
          type="text"
          name="lastName"
          value={formData.lastName}
          placeholder="Inserisci il tuo cognome"
          onChange={handleInputChange}
          required
        />
      </div>
    </div>

    {/* Sezione Destra */}
    <div className="right-section">
      <div className="form-group">
        <label>Password*</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          placeholder="Inserisci la tua password"
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Conferma Password*</label>
        <input
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          placeholder="Reinserisci la password"
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Telefono (opzionale)</label>
        <input
          type="tel"
          name="phone"
          value={formData.phone}
          onChange={handleInputChange}
          placeholder="Formato: +39 012 3456789"
          maxLength="16"
        />
      </div>
      <div className='form-group'>
      <label class="labelButton">* Campi Obbligatori</label>
      <button type="submit" className="register-button">Registrati</button>
      </div>
    </div>
  </div>

  <p className="login-link">
    Hai già un account? <Link to="/login">Accedi</Link>
  </p>
</form>

    </div>
  );
};

export default Register;