import React from 'react';
import { Button } from '@mui/material';
import '../css/LoadChat.css';
import { useTheme } from '@mui/material/styles';
import SendIcon from '@mui/icons-material/Send';
import { useState } from 'react';
import { createChat } from '../utils/MessageHandler';
import Alert from '@mui/material/Alert';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import Collapse from '@mui/material/Collapse';

function LoadChat({userLogged}) {

    const [inputValue, setInputValue] = useState('');
    const [alertVisible, setAlertVisible] = useState(false); 
    const [open, setOpen] = React.useState(true);

    const theme = useTheme();

    const inputChatStyle = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
        color: theme.palette.mode === 'dark' ? 'white' : 'black',
    };

    const buttons = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
        color: theme.palette.mode === 'dark' ? '#333' : 'white',
    };

    const handleCreateChat = () => {
        if (!inputValue.trim()) { 
            setAlertVisible(true)
            setOpen(true)
            return;
        }
        createChat(inputValue); 
        window.location.reload();
    };

    return (
        <>
            <div className="container">

            {alertVisible && (
                <Collapse in={open}>
                <Alert
                    style={{
                        top: '100px',
                        position: 'fixed', 
                        transform: 'translateX(-50%)'
                    }}
                    variant="filled" 
                    severity="error"
                  action={
                    <IconButton
                      aria-label="close"
                      color="inherit"
                      size="small"
                      onClick={() => {
                        setOpen(false);
                      }}
                    >
                      <CloseIcon fontSize="inherit" />
                    </IconButton>
                  }
                  sx={{ mb: 2 }}
                >
                  Attenzione! Riempire il campo 'Titolo' richiesto per avviare una nuova Chat
                </Alert>
              </Collapse>
            )}
                
                <p id='user'>Ciao {userLogged}</p>
                <div className="start">
                    <p className='scope'>Inizia una nuova conversazione</p>
                    <input

                        className='input'
                        type="text"
                        placeholder="Titolo Chat"
                        style={inputChatStyle}
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                    />
                    <Button
                        className='button'
                        endIcon={<SendIcon />}
                        style={buttons}
                        onClick={handleCreateChat} // Add onClick handler
                    >
                        Inizia la conversazione
                    </Button>
                </div>
            </div>
        </>
    );
}

export default LoadChat;
