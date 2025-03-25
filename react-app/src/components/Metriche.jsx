import { useState, useEffect } from 'react';
import '../css/Metriche.css'
import { useTheme } from '@mui/material/styles';
import GetAppIcon from '@mui/icons-material/GetApp';
import { Button } from '@mui/material';

const Metriche = () => {

    const theme = useTheme();

    const cardStyle = {
      backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
      color: theme.palette.mode === 'dark' ? 'white' : 'black', 
    }

    const titles = {
      color: theme.palette.mode === 'dark' ? 'lightgray' : '#333',
    }

    const buttons = {
      backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
      color: theme.palette.mode === 'dark' ? '#333' : 'white', 
    }

  return (
    <div className="metrics-container">
      <h1 style={{paddingBottom: '5px', borderBottom: '1px solid grey', marginBottom: '30px'}}>Dashboard Metriche</h1>
      <Button startIcon={<GetAppIcon />} onClick="" className="export-button" style={buttons}>
        Esporta CSV
      </Button>

      <div className="metrics-grid">
        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Like Totali</h3>
          <p>92834</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Dislike Totali</h3>
          <p>2734</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Totale Messaggi</h3>
          <p>6835103</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Rating Positivo</h3>
          <p>76%</p>
        </div>
      </div>
    </div>
  );
};

export default Metriche;