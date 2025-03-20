import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';
import MuccaIcon from '../assets/mucca.jpg';
import addIcon from '../assets/addfile.svg';
import saveIcon from '../assets/save.svg';
import deleteIcon from '../assets/delete.svg';

function Chatbot() {
  const [count, setCount] = useState(0);


  const endRef = useRef(null);
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [])

  return (
    <>
      <div className="chat">
      <div className="top">
        <div className="user">
          <img src={MuccaIcon} alt="icona di giorgione"/>
          <div className="texts">
            <span>Giorgione</span>
            <p>Lorem ipsum dolor sit amet</p>
          </div>
        </div>
        <div className='icons'>
          <img src={addIcon} />
          <img src={saveIcon} />
          <img src={deleteIcon}/>
        </div>
      </div>
    
      <div className="center">
        <div className="message"> 
          <img src={MuccaIcon} alt="icona di giorgione"/>
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
          <img src={MuccaIcon} alt="icona di giorgione"/>
          <div className="texts">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <span>1 min ago</span>
          </div>
        </div>
        <div ref={endRef}></div>
      </div>
      <div className="bottom">
        <input type="text" placeholder="Scrivi un messaggio..."/>
        <button className="sendButton">Invia</button>
      </div>
      </div>
    </>
  );
}

export default Chatbot;
