import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/landingpage.css';
import mucca from '../assets/mucca.jpg';

const LandingPage = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login'); // Reindirizza alla pagina di login
  };

  return (
    <div className='overlay'>
    <div className="landing-container">
      <header className="landing-header">
        <img src={mucca} alt="icona giorgione" />
        <h1>Giorgione</h1>
        <p>Il tuo assistente AI per scoprire e acquistare i prodotti tipici della Valsana</p>
      </header>
      <main className="landing-main">
        <section className="landing-section">
          <h2>Cosa siamo</h2>
          <p>
            Giorgione è l'intelligenza artificiale che ti guida alla scoperta dei sapori autentici della Valsana.
            Che tu stia cercando formaggi, vini, salumi o altre prelibatezze, Giorgione ti consiglia i migliori
            prodotti locali, direttamente dai produttori della regione.
          </p>
          <button onClick={handleLoginClick} className="login-button">
            Accedi e scopri i prodotti
          </button>
        </section>
      </main>
    </div>
    </div>
  );
};

export default LandingPage;