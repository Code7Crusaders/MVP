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
import { fetchMessages, saveMessage, chatInteract } from '../utils/api'; // Import API functions
import ReactMarkdown from 'react-markdown'; // Importa react-markdown

function Chatbot({ chatId }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
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
    const loadMessages = async () => {
      try {
        const data = await fetchMessages(chatId); // Fetch messages using API function
        setMessages(data);
      } catch (error) {
        console.error('Error loading messages:', error);
      }
    };

    loadMessages();
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
      const savedMessage = await saveMessage(newMessage);
      setMessages((prevMessages) => [
        ...prevMessages,
        { ...newMessage, id: savedMessage.id, created_at: new Date() },
      ]);
      setInputValue('');

      // Call chatInteract to get the bot's response
      const botResponse = await chatInteract(inputValue);

      // Save the bot's response as a message
      const botMessage = {
        text: botResponse.answer,
        conversation_id: chatId,
        rating: null,
        is_bot: true,
      };

      const savedBotMessage = await saveMessage(botMessage);
      setMessages((prevMessages) => [
        ...prevMessages,
        { ...botMessage, id: savedBotMessage.id, created_at: new Date() },
      ]);
    } catch (error) {
      console.error('Failed to send or process message:', error);
    }
  };

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
        {messages.map((message, index) => (
          <div key={message.id || `message-${index}`} className={`message ${message.is_bot ? 'bot' : 'own'}`}>
            <div className="texts">
              {message.is_bot ? (
                // Wrap ReactMarkdown in a container with a specific class
                <div className="markdown-content">
                  <ReactMarkdown>{message.text}</ReactMarkdown>
                </div>
              ) : (
                // Show normal text for user messages
                <p>{message.text}</p>
              )}
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
    </div>
  );
}

Chatbot.propTypes = {
  chatId: PropTypes.string.isRequired,
};

export default Chatbot;
