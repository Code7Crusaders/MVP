import { useEffect, useState, useRef } from 'react';
import '../css/chat.css';
import MuccaIcon from '../assets/mucca.jpg';
import { useTheme } from '@mui/material/styles';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';
import SendIcon from '@mui/icons-material/Send';
import AddIcon from '@mui/icons-material/Add';
import QuickreplyIcon from '@mui/icons-material/Quickreply';
import SaveIcon from '@mui/icons-material/Save';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import { Dialog, DialogContent, DialogActions, TextField, Button, DialogContentText, Alert } from '@mui/material';

function Chatbot() {
  const [count, setCount] = useState(0);
  const [Salvataggio, setSalvataggioOpen] = useState(false); // Stato per gestire il DIALOG di salvataggio
  const [Eliminazione, setEliminazioneOpen] = useState(false); // Stato per gestire il DIALOG dell'eliminazione
  
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

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white', 
  }

  // DIALOG per il salvataggio della chat
  const chiudiDialogSalvataggio = () => {
    setSalvataggioOpen(false); 
  };
  const SalvaChat = () => {
    //controllare che non sia vuoto il titolo
    // Salvataggio della chat
    setSalvataggioOpen(false); 
  };
  const apriDialogSalvataggio = () => {
    setSalvataggioOpen(true); 
  };

  // DIALOG per l'eliminazione della chat
  const chiudiDialogEliminazione = () => {
    setEliminazioneOpen(false); 
  };
  const EliminaChat = () => {
    // Eliminazione della chat
    setEliminazioneOpen(false); 
  };
  const apriDialogEliminazione = () => {
    setEliminazioneOpen(true); 
  };



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
          <button className='btnsTop' alt="aggiungi un template" title='Aggiungi Template' style={buttons}><AddIcon /></button>
          <button className='btnsTop' alt="seleziona template" title='Seleziona domanda' style={buttons}><QuickreplyIcon /></button>
          <button className='btnsTop' alt="Salva la chat" title='Salva Chat' style={buttons} onClick={apriDialogSalvataggio}><SaveIcon /></button>
          <button className='btnsTop' alt="Elimina la chat" title='Elimina Chat' style={buttons} onClick={apriDialogEliminazione}><DeleteForeverIcon /></button>
        </div>
      </div>
    
      <div className="center">
        <div className="message"> 
          <img src={MuccaIcon} alt="icona di giorgione"/>
          <div className="texts">
            <p>Ciao User, come posso esserti utile?</p>
            <span style={timeSpan}>1 min ago</span>
            <div className="feedback">
              <button className='feedbackButton' style={buttons}><ThumbUpIcon /></button>
              <button className='feedbackButton' style={buttons}><ThumbDownIcon /></button>
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
              <button className='feedbackButton' style={buttons}><ThumbUpIcon /></button>
              <button className='feedbackButton' style={buttons}><ThumbDownIcon /></button>
            </div>
          </div>
        </div>
        <div ref={endRef}></div>
      </div>
      <div className="bottom">
      <input  type="text"  placeholder="Scrivi un messaggio..." style={inputChatStyle} />
        <button className='sendButton' style={buttons}><SendIcon  /></button>
      </div>
      </div>

      {/* DIALOG per il salvataggio della chat */}
      <Dialog open={Salvataggio} onClose={chiudiDialogSalvataggio} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '30px', margin: '16px 24px 0 24px', fontWeight: 'bold', }, ...timeSpan }}>Salva Chat</DialogContentText>
        <DialogContentText style={{...{fontSize: '16px', marginLeft:'24px',}, ...timeSpan }}>Inserisci il titolo della conversazione da salvare</DialogContentText>
        <DialogContent>
          <TextField style={{ ...{borderRadius: '8px'}, ...inputChatStyle}}
            placeholder="Titolo Chat"
            fullWidth
          />
        </DialogContent>
        <DialogActions style={{marginBottom: '25px', marginRight: '24px'}}>
          <Button onClick={chiudiDialogSalvataggio} style={buttons}>Annulla</Button>
          <Button onClick={SalvaChat} style={buttons}>Salva chat</Button>
        </DialogActions>
      </Dialog>


      {/* DIALOG per l'eliminazione della chat */}
      <Dialog open={Eliminazione} onClose={chiudiDialogEliminazione}>
      <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...timeSpan }}>Prova di un titolo per questa chat</DialogContentText>
      <DialogContentText style={{ ...{ fontSize: '16px', margin:'6px 24px 0 24px',}, ...timeSpan }}>Sei sicuro di voler eliminare questa conversazione?</DialogContentText>
        <DialogActions style={{margin: '10px 16px 20px 0'}}>
          <Button onClick={chiudiDialogEliminazione} style={buttons}>Annulla</Button>
          <Button onClick={EliminaChat} style={buttons}>Elimina chat</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default Chatbot;
