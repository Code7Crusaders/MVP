import { useState } from 'react';
import '../css/chat.css';

function Chatbot() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="Chat">
      <div className="Top">
        <div className="user">
          <img src="#" alt="icona di giorgione"/>
          <div className="texts">
            <span>Giorgione</span>
            <p>Lorem ipsum dolor sit amet</p>
          </div>
        </div>
      </div>
      <div className="center"></div>
      <div className="Bottom">
        <div className="icons">
          <img src="#" alt="icona di allegato"/>
        </div>
        <input type="text" placeholder="Scrivi un messaggio..."/>
        <button className="sendButton">Invia</button>
      </div>
      </div>
    </>
  );
}

export default Chatbot;
