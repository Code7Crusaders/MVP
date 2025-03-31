import { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
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
import ReactMarkdown from 'react-markdown';
import {
  loadMessages,
  saveNewMessage,
  handleFeedback,
  interactWithChat,
  updateFeedback,
  deleteChat,
} from '../utils/MessageHandler';
import { Dialog, DialogContent, DialogActions, TextField, DialogContentText, Alert } from '@mui/material';
import { Button } from '@mui/material';


function Chatbot({ chatId, chatTitle }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [Eliminazione, setEliminazioneOpen] = useState(false);
  const navigate = useNavigate();


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

  // DIALOG per l'eliminazione della Chat
  const chiudiDialogEliminazione = () => {
    setEliminazioneOpen(false);
  };

  const EliminaChat = () => {
    deleteChat(chatId);
    setEliminazioneOpen(false);
    window.location.reload();
  };

  const apriDialogEliminazione = () => {
    setEliminazioneOpen(true);
  };

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const loadedMessages = await loadMessages(chatId);
        setMessages(loadedMessages);
      } catch (error) {
        console.error('Error loading messages:', error);
      }
    };

    fetchMessages();
  }, [chatId]);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const newMessage = {
      text: inputValue,
      conversation_id: chatId,
      rating: null,
      is_bot: false,
    };

    try {
      // Save the user's message
      const savedMessage = await saveNewMessage(newMessage);
      setMessages((prevMessages) => [...prevMessages, savedMessage]);
      setInputValue('');

      // Interact with the chat and save the bot's response
      const botMessage = await interactWithChat(inputValue, chatId);
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Failed to send or process message:', error);
    }
  };

  const handleFeedbackClick = async (messageId, isPositive) => {
    try {
      // Aggiorna la valutazione nel database chiamando updateFeedback
      await updateFeedback(messageId, isPositive);

      // Aggiorna lo stato locale dei messaggi
      setMessages((prevMessages) =>
        prevMessages.map((msg) =>
          msg.id === messageId ? { ...msg, selectedRating: isPositive } : msg
        )
      );

    } catch (error) {
      console.error('Errore durante il click sul feedback:', error);
    }
  };


  return (
    <div className="chat">
      <div className="top">
        <div className="title">
          <p>{chatTitle || 'Chat'}</p> {/* Display the chat title */}
        </div>
        <div className="icons">
          <Tooltip title="Templates" placement="bottom">
            <button className="btnsTop" style={buttons}>
              <QuickreplyIcon />
            </button>
          </Tooltip>
          <Tooltip title="Elimina Chat" placement="bottom">
            <button className="btnsTop" style={buttons} onClick={apriDialogEliminazione}>
              <DeleteForeverIcon />
            </button>
          </Tooltip>
        </div>
      </div>

      <div className="center">
        {messages.map((message, index) => (
          <div key={message.id || `message-${index}`} className={`message ${message.is_bot ? 'bot' : 'own'}`}>
            <div className="texts">
              {message.is_bot ? (
                <div className="markdown-content">
                  <ReactMarkdown>{message.text}</ReactMarkdown>
                </div>
              ) : (
                <p>{message.text}</p>
              )}
              <span style={timeSpan}>{new Date(message.created_at).toLocaleString()}</span>
              {message.is_bot && (
                <div className="feedback">
                  <button
                    className={`feedbackButton ${message.selectedRating === true ? 'selected thumbs-up' : ''}`}
                    onClick={async () => {
                      try {
                        await handleFeedbackClick(message.id, true);
                      } catch (error) {
                        console.error('Error handling thumbs-up feedback:', error);
                      }
                    }}
                  >
                    <ThumbUpIcon />
                  </button>
                  <button
                    className={`feedbackButton ${message.selectedRating === false ? 'selected thumbs-down' : ''}`}
                    onClick={async () => {
                      try {
                        await handleFeedbackClick(message.id, false);
                      } catch (error) {
                        console.error('Error handling thumbs-down feedback:', error);
                      }
                    }}
                  >
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
        <input
          type="text"
          placeholder="Scrivi un messaggio..."
          style={inputChatStyle}
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button className="sendButton" style={buttons} onClick={handleSendMessage}>
          <SendIcon />
        </button>
      </div>

      {/* DIALOG per l'eliminazione della chat */}
      <Dialog open={Eliminazione} onClose={chiudiDialogEliminazione}>
        <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...timeSpan }}>TITOLO CHAT</DialogContentText>
        <DialogContentText style={{ ...{ fontSize: '16px', margin: '6px 24px 0 24px', }, ...timeSpan }}>Sei sicuro di voler eliminare questa conversazione?</DialogContentText>
        <DialogActions style={{ margin: '10px 16px 20px 0' }}>
          <Button onClick={chiudiDialogEliminazione} style={buttons}>Annulla</Button>
          <Button onClick={EliminaChat} style={buttons}>Elimina Chat</Button>
        </DialogActions>
      </Dialog>

    </div>
  );
}

Chatbot.propTypes = {
  chatId: PropTypes.string.isRequired,
  chatTitle: PropTypes.string.isRequired, // Add prop type for chatTitle
};

export default Chatbot;
