import { useState } from 'react';
import '../css/RichiestaSupporto.css';
import { useTheme } from '@mui/material/styles';

const RichiestaSupporto = () => {

  const theme = useTheme();

  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
    fontFamily: theme.typography.fontFamily,
            '::placeholder': {
              color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',
              fontFamily: theme.typography.fontFamily,} 
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  }

  const timeSpan = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  }

  const [formData, setFormData] = useState({
    user_id: '',
    subject: '',
    description: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/api/support', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...formData,
          user_id: Number(formData.user_id), // Converti in numero
        }),
      });

      if (!response.ok) {
        throw new Error('Errore durante l\'invio della richiesta');
      }

      setSuccess(true);
      setFormData({ user_id: '', subject: '', description: '' });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="support-form-container">
      <h1>Contatta l'assistenza</h1>
      {success && <div className="success-message">Richiesta inviata con successo!</div>}
      {error && <div className="error-message">{error}</div>}

      <form onSubmit={handleSubmit}>

        <div className="form-group">
          <label style={timeSpan} htmlFor="subject">Oggetto:</label>
          <input
            type="text"
            id="subject"
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            required
            maxLength="255"
            placeholder="Inserisci l'oggetto della tua richiesta di supporto"
            style={inputChatStyle}
          />
        </div>

        <div className="form-group">
          <label style={timeSpan} htmlFor="description">Descrizione:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
            rows="5"
            placeholder='Inserisci il contenuto della tua richiesta di supporto'
            style={inputChatStyle}
          />
        </div>

        <button style={buttons} className='bottoneSupporto' type="submit" disabled={loading}>
          {loading ? 'Invio in corso...' : 'Invia richiesta'}
        </button>
      </form>
    </div>
  );
};

export default RichiestaSupporto;