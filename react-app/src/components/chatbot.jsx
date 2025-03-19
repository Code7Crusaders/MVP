import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';

function Chatbot() {
  const [count, setCount] = useState(0);


  const endRef = useRef(null);
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [])

  return (
    <>
      <div className="Chat">
      <div className="Top">
        <div className="user">
          <img src="https://avatars.githubusercontent.com/u/185105956?s=200&v=4" alt="icona di giorgione"/>
          <div className="texts">
            <span>Giorgione</span>
            <p>Lorem ipsum dolor sit amet</p>
          </div>
        </div>
      </div>
    
      <div className="center">
        <div className="message"> 
          <img src="https://avatars.githubusercontent.com/u/185105956?s=200&v=4" alt="icona di giorgione"/>
          <div className="texts">
            <p>Ciao User, come posso esserti utile?</p>
            <span>1 min ago</span>
          </div>
        </div>
        <div className="message own"> 
          <div className="texts">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
            <span>1 min ago</span>
          </div>
        </div>
        <div className="message"> 
          <img src="https://avatars.githubusercontent.com/u/185105956?s=200&v=4" alt="icona di giorgione"/>
          <div className="texts">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <span>1 min ago</span>
          </div>
        </div>
        <div ref={endRef}></div>
      </div>
      <div className="Bottom">
        <div className="icons">
          <img src="../assets/addfile.svg" alt="icona di allegato"/>
        </div>
        <input type="text" placeholder="Scrivi un messaggio..."/>
        <button className="sendButton">Invia</button>
      </div>
      </div>
    </>
  );
}

export default Chatbot;
