import { useState, useEffect } from 'react';
import '../css/Metriche.css';
import { useTheme } from '@mui/material/styles';
import GetAppIcon from '@mui/icons-material/GetApp';
import { Button } from '@mui/material';
import { fetchDashboardMetrics } from '../utils/api'; // Importa la funzione fetchDashboardMetrics

const Metriche = () => {
  const theme = useTheme();
  const [metrics, setMetrics] = useState({
    totalLikes: 0,
    totalDislikes: 0,
    totalMessages: 0,
    positiveRating: '0%',
  });

  useEffect(() => {
    const loadMetrics = async () => {
      try {
        const data = await fetchDashboardMetrics();
        setMetrics({
          totalLikes: data.total_likes,
          totalDislikes: data.total_dislikes,
          totalMessages: data.total_messages,
          positiveRating: `${data.positive_rating}%`,
        });
      } catch (error) {
        console.error('Errore durante il caricamento delle metriche:', error);
      }
    };

    loadMetrics();
  }, []);

  const cardStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  const titles = {
    color: theme.palette.mode === 'dark' ? 'lightgray' : '#333',
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  };

  return (
    <div className="metrics-container">
      <h1 style={{ paddingBottom: '5px', borderBottom: '1px solid grey', marginBottom: '30px' }}>
        Dashboard Metriche
      </h1>

      <div className="metrics-grid">
        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Like Totali</h3>
          <p>{metrics.totalLikes}</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Dislike Totali</h3>
          <p>{metrics.totalDislikes}</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Totale Messaggi</h3>
          <p>{metrics.totalMessages}</p>
        </div>

        <div className="metric-card" style={cardStyle}>
          <h3 style={titles}>Rating Positivo</h3>
          <p>{metrics.positiveRating}</p>
        </div>
      </div>
    </div>
  );
};

export default Metriche;