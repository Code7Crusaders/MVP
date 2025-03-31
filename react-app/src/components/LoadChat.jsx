import { Button } from '@mui/material';
import '../css/LoadChat.css';
import { useTheme } from '@mui/material/styles';
import SendIcon from '@mui/icons-material/Send';
import { useState } from 'react';
import { createChat } from '../utils/MessageHandler';

function LoadChat() {

    const [inputValue, setInputValue] = useState('');

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
        createChat(inputValue); // Call createChat with the inputValue
        window.location.reload(); 
    };

    return (
        <>
            <div className="container">
                <p id='user'>Ciao User</p>
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
