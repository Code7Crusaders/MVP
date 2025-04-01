import React from 'react';
import { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/chat.css';
import { useTheme } from '@mui/material/styles';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';
import SendIcon from '@mui/icons-material/Send';
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
import QuizIcon from '@mui/icons-material/Quiz';
import Popover from '@mui/material/Popover';

function Chatbot({ chatId, chatTitle }) {
  const [messages, setMessages] = useState([]); // State to store chat messages
  const [inputValue, setInputValue] = useState(''); // State for the input field value
  const [loading, setLoading] = useState(false); // State for loading indicator
  const [Eliminazione, setEliminazioneOpen] = useState(false); // State for delete confirmation dialog
  const [Templates, setTemplatesOpen] = useState(false)
  const [anchorEl, setAnchorEl] = useState(null);  
  const btnTemplateRef = useRef(null);

  const navigate = useNavigate();

  const theme = useTheme(); // Access the current theme
  const endRef = useRef(null); // Reference to scroll to the bottom of the chat

  // Styles for the input field
  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  // Styles for buttons
  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  };

  const timeSpan = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };



  // Close the delete confirmation dialog
  const chiudiDialogEliminazione = () => {
    setEliminazioneOpen(false);
  };

  // Delete the chat and reload the page
  const EliminaChat = () => {
    deleteChat(chatId);
    setEliminazioneOpen(false);
    window.location.reload();
  };

  // Open the delete confirmation dialog
  const apriDialogEliminazione = () => {
    setEliminazioneOpen(true);
  };



  const apriTemplates = () => {
    setTemplatesOpen(true)
    setAnchorEl(btnTemplateRef.current);
  };

  const chiudiTemplates = () => {
    setTemplatesOpen(false)
    setAnchorEl(null);
  };


  // Fetch messages when the component mounts or chatId changes
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

  // Scroll to the bottom of the chat when messages change
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Handle sending a new message
  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const newMessage = {
      text: inputValue,
      conversation_id: chatId,
      rating: null,
      is_bot: false,
    };

    try {
      // Add the user's message
      const savedMessage = await saveNewMessage(newMessage);
      setMessages((prevMessages) => [...prevMessages, savedMessage]);
      setInputValue('');

      // Set loading state
      setLoading(true);

      // Interact with the chatbot and save the response
      const botMessage = await interactWithChat(inputValue, chatId);
      setMessages((prevMessages) => [...prevMessages, botMessage]);

    } catch (error) {
      console.error('Failed to send or process message:', error);
    } finally {
      // Remove loading state
      setLoading(false);
    }
  };

  // Handle feedback click (thumbs up or down)
  const handleFeedbackClick = async (messageId, isPositive) => {
    try {
      // Update feedback in the database
      await updateFeedback(messageId, isPositive);

      // Update local state of messages
      setMessages((prevMessages) =>
        prevMessages.map((msg) =>
          msg.id === messageId ? { ...msg, selectedRating: isPositive } : msg
        )
      );

    } catch (error) {
      console.error('Error handling feedback click:', error);
    }
  };


  const [selectedQuestion, setSelectedQuestion] = useState(null);
  const questions = [
    { id: 1, text: "Cos'è React?" },
    { id: 2, text: "Come funziona il Virtual DOM?" },
    { id: 3, text: "Che differenza c'è tra state e props?" },
    { id: 4, text: "Come si crea un componente in React?" },
    { id: 5, text: "Cos'è JSX?" },
    { id: 6, text: "Come si gestiscono gli eventi in React?" },
    { id: 7, text: "Che cos'è un Hook in React?" },
    { id: 8, text: "A cosa serve useEffect?" },
    { id: 9, text: "Come si ottimizza le prestazioni in React?" },
    { id: 10, text: "Cos'è il Context API?" },
  ];



  return (
    <div className="chat">
      <div className="top">
        <div className="title">
          <p>{chatTitle || 'Chat'}</p> {/* Display the chat title */}
        </div>
        <div className="icons">
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

        {/* Loading indicator */}
        {loading && (
          <div className="typing-indicator">
          <span><b>Giorgione</b> sta scrivendo &nbsp;</span>
          <div className="dot-container">
            <div className="dot"></div>
            <div className="dot"></div>
            <div className="dot"></div>
          </div>
          </div>
        )}

        <div ref={endRef}></div>
      </div>

      <div className="bottom">
        <button ref={btnTemplateRef} className="btnTemplate" onClick={apriTemplates} >
          <QuizIcon />
        </button>

        <input
          type="text"
          placeholder="Scrivi un messaggio..."
          style={inputChatStyle}
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              handleSendMessage();
            }
          }}
        />
        <button className="sendButton" style={buttons} onClick={handleSendMessage}>
          <SendIcon />
        </button>
      </div>

      {/* Dialog for chat deletion */}
      <Dialog open={Eliminazione} onClose={chiudiDialogEliminazione}>
        <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...timeSpan }}>{chatTitle || 'Chat'}</DialogContentText>
        <DialogContentText style={{ ...{ fontSize: '16px', margin: '6px 24px 0 24px', }, ...timeSpan }}>Sei sucuro di voler cancellare questa Chat?</DialogContentText>
        <DialogActions style={{ margin: '10px 16px 20px 0' }}>
          <Button onClick={chiudiDialogEliminazione} style={buttons}>Annulla</Button>
          <Button onClick={EliminaChat} style={buttons}>Elimina Chat</Button>
        </DialogActions>
      </Dialog>


      
      <Popover
        open={Templates}
        onClose={chiudiTemplates}
        anchorEl={anchorEl} // Passiamo l'elemento ancorato
        anchorOrigin={{
          vertical: 'top', // Posiziona il popover sotto il bottone
          horizontal: 'left', // Centrato orizzontalmente
        }}
        transformOrigin={{
          vertical: 'bottom', // Il popover si apre sopra il bottone
          horizontal: 'left', // Centrato orizzontalmente
        }}
      >
        <div className="questions-container">
      <h2>Domande Templates</h2>
      <div className="questions-list">
        {questions.map((question) => (
          <div 
            key={question.id}
            className={`question-item ${selectedQuestion === question.id ? 'selected' : ''}`}
          >
            <span>{question.text}</span>
            <button 
              className="action-btn"
              onClick={(e) => {
                e.stopPropagation()
                chiudiTemplates()
                setInputValue(question.text)
              }}
            >
              Invia
            </button>
          </div>
        ))}
      </div>
    </div>
      </Popover>

    </div>
  );
}

Chatbot.propTypes = {
  chatId: PropTypes.string.isRequired, // Chat ID is required
  chatTitle: PropTypes.string.isRequired, // Chat title is required
};

export default Chatbot;
