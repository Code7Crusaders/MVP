import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';
import { useTheme } from '@mui/material/styles';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';
import SendIcon from '@mui/icons-material/Send';
import QuickreplyIcon from '@mui/icons-material/Quickreply';
import SaveIcon from '@mui/icons-material/Save';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import { Tooltip } from '@mui/material';
import PropTypes from 'prop-types';

function Chatbot({ chatId }) {
  const [messages, setMessages] = useState([]);
  const [salvataggioOpen, setSalvataggioOpen] = useState(false);
  const [eliminazioneOpen, setEliminazioneOpen] = useState(false);

  const theme = useTheme();
  const endRef = useRef(null);

  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  };

  const timeSpan = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch(`http://127.0.0.1:5000/message/get_by_conversation/${chatId}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!response.ok) {
          throw new Error('Failed to fetch messages');
        }
        const data = await response.json();
        console.log('Fetched messages:', data); // Debugging log
        setMessages(data);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    };

    fetchMessages();
  }, [chatId]);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="chat">
      <div className="top">
        <div className="title">
          <p>Chat ID: {chatId}</p>
        </div>
        <div className="icons">
          <Tooltip title="Templates" placement="bottom">
            <button className="btnsTop" style={buttons}>
              <QuickreplyIcon />
            </button>
          </Tooltip>
          <Tooltip title="Salva Chat" placement="bottom">
            <button className="btnsTop" style={buttons} onClick={() => setSalvataggioOpen(true)}>
              <SaveIcon />
            </button>
          </Tooltip>
          <Tooltip title="Elimina Chat" placement="bottom">
            <button className="btnsTop" style={buttons} onClick={() => setEliminazioneOpen(true)}>
              <DeleteForeverIcon />
            </button>
          </Tooltip>
        </div>
      </div>

      <div className="center">
        {messages.map((message) => (
          <div key={message.id} className={`message ${message.is_bot ? 'bot' : 'own'}`}>
            <div className="texts">
              <p>{message.text}</p>
              <span style={timeSpan}>{new Date(message.created_at).toLocaleString()}</span>
              {message.is_bot && (
                <div className="feedback">
                  <button className="feedbackButton" style={buttons}>
                    <ThumbUpIcon />
                  </button>
                  <button className="feedbackButton" style={buttons}>
                    <ThumbDownIcon />
                  </button>
                </div>
              )}
            </div>
          </div>
        ))}
        <div ref={endRef}></div>
      </div>

      <div className="bottom">
        <input type="text" placeholder="Scrivi un messaggio..." style={inputChatStyle} />
        <button className="sendButton" style={buttons}>
          <SendIcon />
        </button>
      </div>
    </div>
  );
}

Chatbot.propTypes = {
  chatId: PropTypes.string.isRequired,
};

export default Chatbot;
