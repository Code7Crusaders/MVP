import { useState } from 'react';
import '../css/RichiestaSupporto.css';
import { useTheme } from '@mui/material/styles';

const RichiestaSupporto = () => {

  const theme = useTheme();
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
          <label htmlFor="subject">Oggetto:</label>
          <input
            type="text"
            id="subject"
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            required
            maxLength="255"
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Descrizione:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
            rows="5"
          />
        </div>

        <button className='bottoneSupporto' type="submit" disabled={loading}>
          {loading ? 'Invio in corso...' : 'Invia richiesta'}
        </button>
      </form>
    </div>
  );
};

export default RichiestaSupporto;