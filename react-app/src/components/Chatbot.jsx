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
import { fetchTemplateList } from '../utils/api'; // Importa fetchTemplateList

function Chatbot({ chatId, chatTitle }) {
  const [messages, setMessages] = useState([]); // Stato per i messaggi
  const [inputValue, setInputValue] = useState(''); // Stato per il valore dell'input
  const [loading, setLoading] = useState(false); // Stato per il caricamento
  const [Eliminazione, setEliminazioneOpen] = useState(false); // Stato per il dialog di eliminazione
  const [Templates, setTemplatesOpen] = useState(false); // Stato per il popover dei template
  const [anchorEl, setAnchorEl] = useState(null); // Elemento ancorato per il popover
  const [templateList, setTemplateList] = useState([]); // Stato per la lista dei template
  const btnTemplateRef = useRef(null);

  const navigate = useNavigate();
  const theme = useTheme(); // Accesso al tema corrente
  const endRef = useRef(null); // Riferimento per scrollare in fondo alla chat

  // Recupera i template dal backend quando il componente viene montato
  useEffect(() => {
    const fetchTemplates = async () => {
      try {
        const templates = await fetchTemplateList();
        setTemplateList(templates); // Salva i template nello stato
      } catch (error) {
        console.error('Errore nel recupero dei template:', error);
      }
    };

    fetchTemplates();
  }, []);

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
    setTemplatesOpen(true);
    setAnchorEl(btnTemplateRef.current);
  };

  const chiudiTemplates = () => {
    setTemplatesOpen(false);
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

      // Controlla se il messaggio è un template
      const selectedTemplate = templateList.find((template) => template.question === inputValue);
      if (selectedTemplate) {
        // Mostra la risposta del template come messaggio bot
        const botMessage = {
          text: selectedTemplate.answer,
          conversation_id: chatId,
          rating: null,
          is_bot: true,
          created_at: new Date(),
        };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      } else {
        // Se non è un template, chiama il modello LLM
        setLoading(true);
        const botMessage = await interactWithChat(inputValue, chatId);
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }
    } catch (error) {
      console.error('Errore durante l\'invio o l\'elaborazione del messaggio:', error);
    } finally {
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
          <h2>Domande Predefinite</h2>
          <div className="questions-list">
            {templateList.map((template) => (
              <div
                key={template.id}
                className={`question-item ${selectedQuestion === template.id ? 'selected' : ''}`}
              >
                <span>{template.question}</span>
                <button
                  className="action-btn"
                  onClick={async (e) => {
                    e.stopPropagation();
                    chiudiTemplates();

                    try {
                      // Salva la domanda come messaggio utente
                      const userMessage = {
                        text: template.question,
                        conversation_id: chatId,
                        rating: null,
                        is_bot: false,
                        created_at: new Date(),
                      };
                      const savedUserMessage = await saveNewMessage(userMessage);
                      setMessages((prevMessages) => [...prevMessages, savedUserMessage]);

                      // Salva la risposta come messaggio bot
                      const botMessage = {
                        text: template.answer,
                        conversation_id: chatId,
                        rating: null,
                        is_bot: true,
                        created_at: new Date(),
                      };
                      const savedBotMessage = await saveNewMessage(botMessage);
                      setMessages((prevMessages) => [...prevMessages, savedBotMessage]);
                    } catch (error) {
                      console.error('Errore durante il salvataggio dei messaggi templatizzati:', error);
                    }
                  }}
                >
                  Seleziona 
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
