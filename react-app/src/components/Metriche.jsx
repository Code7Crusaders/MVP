import { useState, useEffect } from 'react';
import '../css/Metriche.css'
import { useTheme } from '@mui/material/styles';

const Metriche = () => {

    const theme = useTheme();

  return (
    <div className="metrics-container">
      <h1>Dashboard Metriche</h1>
      <button onClick="" className="export-button">
        Esporta CSV
      </button>

      <div className="metrics-grid">
        <div className="metric-card">
          <h3>Like Totali</h3>
          <p></p>
        </div>

        <div className="metric-card">
          <h3>Dislike Totali</h3>
          <p></p>
        </div>

        <div className="metric-card">
          <h3>Totale Messaggi</h3>
          <p></p>
        </div>

        <div className="metric-card">
          <h3>Rating Positivo</h3>
          <p></p>
        </div>
      </div>
    </div>
  );
};

export default Metriche;