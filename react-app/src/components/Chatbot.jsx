import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';
import MuccaIcon from '../assets/mucca.jpg';
import addIcon from '../assets/addfile.svg';
import saveIcon from '../assets/save.svg';
import deleteIcon from '../assets/delete.svg';
import answIcon from '../assets/answ.svg';
import { useTheme } from '@mui/material/styles';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';

function Chatbot() {
  const [count, setCount] = useState(0);
  
  const theme = useTheme();
  
  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
            '::placeholder': {
              color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',} 
  };

  const timeSpan = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  }

  const feedbackButtons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  }

  const endRef = useRef(null);
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [count]);  

  return (
    <>
      <div className="chat">
      <div className="top">
        <div className="title">
          <p>Prova di un titolo per questa chat</p>
        </div>
        <div className='icons' >
          <img src={addIcon} className='btnsTop' alt="aggiungi un template" title='Aggiungi Template'/>
          <img src={answIcon} className='btnsTop' alt="seleziona template" title='Seleziona domanda'/>
          <img src={saveIcon} className='btnsTop' alt="Salva la chat" title='Salva Chat'/>
          <img src={deleteIcon} className='btnsTop' alt="Elimina la chat" title='Elimina Chat'/>
        </div>
      </div>
    
      <div className="center">
        <div className="message"> 
          <img src={MuccaIcon} alt="icona di giorgione"/>
          <div className="texts">
            <p>Ciao User, come posso esserti utile?</p>
            <span style={timeSpan}>1 min ago</span>
            <div className="feedback">
              <button className='feedbackButton' style={feedbackButtons}><ThumbUpIcon /></button>
              <button className='feedbackButton' style={feedbackButtons}><ThumbDownIcon /></button>
            </div>
          </div>
        </div>
        <div className="message own"> 
          <div className="texts">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
            <span style={timeSpan}>1 min ago</span>
          </div>
        </div>
        <div className="message"> 
          <img src={MuccaIcon} alt="icona di giorgione"/>
          <div className="texts">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <span style={timeSpan}>1 min ago</span>
            <div className="feedback">
              <button className='feedbackButton' style={feedbackButtons}><ThumbUpIcon /></button>
              <button className='feedbackButton' style={feedbackButtons}><ThumbDownIcon /></button>
            </div>
          </div>
        </div>
        <div ref={endRef}></div>
      </div>
      <div className="bottom">
      <input  type="text"  placeholder="Scrivi un messaggio..." style={inputChatStyle} />
        <button className='sendButton'>Invia</button>
      </div>
      </div>
    </>
  );
}

export default Chatbot;
