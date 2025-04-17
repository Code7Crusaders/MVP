import React from 'react';
import { useState } from 'react';
import '../css/RichiestaSupporto.css';
import { useTheme } from '@mui/material/styles';
import { sendSupportRequest } from '../utils/SupportMessageHandler'; // Import the utility function
import { saveSupportMessage } from '../utils/api';
import Alert from '@mui/material/Alert';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import Collapse from '@mui/material/Collapse';

const saveSupportRequest = async (formData) => {
  try {
    const response = await sendSupportRequest(formData); // Use the utility function
    if (!response.ok) {
      throw new Error('Errore durante l\'invio della richiesta');
    }
    return response;
  } catch (error) {
    console.error('Errore durante il salvataggio della richiesta di supporto:', error);
    throw error;
  }
};

const RichiestaSupporto = () => {
  const theme = useTheme();

  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
    fontFamily: theme.typography.fontFamily,
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  };

  const timeSpan = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  const [formData, setFormData] = useState({
    user_id: '',
    subject: '',
    description: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const [open, setOpen] = React.useState(true);


  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const supportMessageData = {
      description: formData.description,
      subject: formData.subject,
    };

    try {
      const response = await saveSupportMessage(supportMessageData);
      console.log('Response:', response);
      setSuccess(true);
      setOpen(true)
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
      <h1 style={{ paddingBottom: '5px', borderBottom: '1px solid grey', marginBottom: '30px' }}>
        Contatta l'assistenza
      </h1>
      {success && <Collapse in={open}>
                <Alert
                    variant="filled" 
                    severity="success"
                  action={
                    <IconButton
                      aria-label="close"
                      color="inherit"
                      size="small"
                      onClick={() => {
                        setOpen(false);
                      }}
                    >
                      <CloseIcon fontSize="inherit" />
                    </IconButton>
                  }
                  sx={{ mb: 2 }}
                >
                  Richiesta inviata con successo!
                </Alert>
              </Collapse>}
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
            placeholder="Inserisci il contenuto della tua richiesta di supporto"
            style={inputChatStyle}
          />
        </div>

        <button style={buttons} className="bottoneSupporto" type="submit" disabled={loading}>
          {loading ? 'Invio...' : 'Invia'}
        </button>
      </form>
    </div>
  );
};

export default RichiestaSupporto;