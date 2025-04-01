import { useEffect, useState } from 'react';
import { fetchSupportMessages } from '../utils/SupportMessageHandler';
import '../css/chat.css';
import { useTheme } from '@mui/material/styles';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import ReplyIcon from '@mui/icons-material/Reply';
import '../css/Assistenza.css';
import MarkEmailReadIcon from '@mui/icons-material/MarkEmailRead';
import { Tooltip } from '@mui/material';

const SupportRequests = () => {
  const theme = useTheme();
  const [supportMessages, setSupportMessages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
    '&::placeholder': {
      color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',
    },
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  };

  useEffect(() => {
    const loadSupportMessages = async () => {
      try {
        const messages = await fetchSupportMessages();
        setSupportMessages(messages);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadSupportMessages();
  }, []);

  if (loading) {
    return <div>Caricamento in corso...</div>;
  }

  if (error) {
    return <div>Errore: {error}</div>;
  }

  return (
    <div className="support-container">
      <h1>Richieste di Assistenza</h1>

      <div className="request-list">
        {supportMessages.map((message) => (
          <div key={message.id} className="request-item" style={inputChatStyle}>
            <div className="statusContainer">
            <div
              className="status-dot"
              style={{
                backgroundColor: message.status ? 'green' : 'red',
              }}
            />
            </div>
            
            <div className="request-info">
              <div className="userdate">
                <span className="request-category">{message.user_id}</span>
                <span className="separator">|</span>
                <span className="request-date">{new Date(message.created_at).toLocaleDateString()}</span>
              </div>
                
              <div className="request-header">
                <span className="request-title">{message.subject}</span>
              </div>
              <div className="request-description">{message.description}</div>
            </div>

            <div className="buttonsContainer">
            <div className="icons">
                <button
                  alt="Rispondi alla richiesta di assistenza"
                  title="Rispondi alla richiesta"
                  style={buttons}
                >
                  <MarkEmailReadIcon />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SupportRequests;