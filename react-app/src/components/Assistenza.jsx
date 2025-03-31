import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';
import { useTheme } from '@mui/material/styles';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import ReplyIcon from '@mui/icons-material/Reply';
import '../css/Assistenza.css';

const SupportRequests = () => {
    const theme = useTheme();

    const inputChatStyle = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
        color: theme.palette.mode === 'dark' ? 'white' : 'black',
        '&::placeholder': {
          color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',} 
      };
      const buttons = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
        color: theme.palette.mode === 'dark' ? '#333' : 'white', 
      }

  const [requests] = useState([
    {
      id: 1,
      title: "Problema di accesso",
      date: "2023-03-15",
      username: "user",
      status: "red",
      description: "Utente non riesce ad accedere al portale"
    },
    {
      id: 2,
      title: "Aggiornamento software",
      date: "2023-03-14",
      username: "jhonny",
      status: "green",
      description: "Richiesta aggiornamento versione 2.3.5"
    },
    {
      id: 3,
      title: "Configurazione email",
      date: "2023-03-13",
      username: "Cristiano Ronaldo",
      status: "red",
      description: "Assistenza configurazione client di posta"
    }
  ]);

  return (
    <div className="support-container">
      <h1>Richieste di Assistenza</h1>
      
      <div className="request-list">
        {requests.map((request) => (
          <div key={request.id} className="request-item" style={inputChatStyle}>
            <div className={`status-dot ${request.status}`} />
            <div className="request-info">
              <div className="request-header">
                <span className="request-title">{request.title}</span>
                <span className="separator">|</span>
                <span className="request-category">{request.username}</span>
                <span className="separator">|</span>
                <span className="request-date">{request.date}</span>
              </div>
              <div className="request-description">
                {request.description}
              </div>
                <div className='icons'>
                    <button alt="Elimina richiesta assistenza" title='Elimina richiesta assistenza' style={buttons}><DeleteForeverIcon/></button>
                    <button al="Rispondi alla richiesta di assistenza" title="Rispondi alla richiesta" style={buttons}><ReplyIcon/></button>
                </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SupportRequests;