import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import '../css/Templates.css';
import { useTheme } from '@mui/material/styles';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import Button from '@mui/material/Button';
import styled from '@mui/material/styles/styled';
import AddBoxIcon from '@mui/icons-material/AddBox';
import { AccordionActions, Tooltip } from '@mui/material';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import { useState, useEffect } from 'react';
import { Dialog, DialogContent, DialogActions, TextField, DialogContentText, Alert } from '@mui/material';
import { fetchTemplateList, deleteTemplate, saveTemplate } from '../utils/api';

function Templates() {
  const [AggiuntaTemplate, setAggTemplateOpen] = useState(false);
  const [Modifica, setModificaOpen] = useState(false);
  const [Eliminazione, setEliminazioneOpen] = useState(false);
  const [templates, setTemplates] = useState([]);
  const [selectedTemplateId, setSelectedTemplateId] = useState(null);

  const theme = useTheme();

  const backTemplate = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(0, 9, 28)' : '#f0f0f0',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  };

  const buttons = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
    color: theme.palette.mode === 'dark' ? '#333' : 'white',
  }

  const textStyle = {
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
  }

  const inputChatStyle = {
    backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
    color: theme.palette.mode === 'dark' ? 'white' : 'black',
    fontFamily: theme.typography.fontFamily,
    '&::placeholder': {
      color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',
    }

  }


  const handleDeleteTemplate = async () => {
    if (!selectedTemplateId) return;

    try {
      await deleteTemplate(selectedTemplateId);
      setTemplates((prevTemplates) =>
        prevTemplates.filter((template) => template.id !== selectedTemplateId)
      );
      setEliminazioneOpen(false);
      setSelectedTemplateId(null);
    } catch (error) {
      console.error('Errore durante l\'eliminazione del template:', error);
    }
  };

  const apriDialogEliminazione = (templateId) => {
    setSelectedTemplateId(templateId);
    setEliminazioneOpen(true);
  };

  const chiudiDialogEliminazione = () => {
    setEliminazioneOpen(false);
    setSelectedTemplateId(null);
  };


  const chiudiDialogAggiuntaTemplate = () => {
    setAggTemplateOpen(false);
  };

  const AggiungiTemplate = async () => {
    const domanda = document.querySelector('input[placeholder="Domanda"]').value;
    const risposta = document.querySelector('textarea[placeholder="Risposta"]').value;

    if (!domanda || !risposta) {
      alert('Compila tutti i campi!');
      return;
    }

    const nuovoTemplate = {
      question: domanda,
      answer: risposta,
    };

    try {
      await saveTemplate(nuovoTemplate);
      const updatedTemplates = await fetchTemplateList();
      setTemplates(updatedTemplates);
      setAggTemplateOpen(false);
    } catch (error) {
      console.error('Errore durante il salvataggio del template:', error);
      alert('Errore durante il salvataggio del template.');
    }
  };

  const apriDialogAggiuntaTemplate = () => {
    setAggTemplateOpen(true);
  };


  const chiudiDialogModifica = () => {
    setModificaOpen(false);
  };

  const ModificaTemplate = async () => {
    if (!selectedTemplateId) {
      alert('Errore: Nessun template selezionato per la modifica.');
      return;
    }

    const domanda = document.querySelector('input[placeholder="Domanda"]').value;
    const risposta = document.querySelector('textarea[placeholder="Risposta"]').value;

    if (!domanda || !risposta) {
      alert('Compila tutti i campi!');
      return;
    }

    const nuovoTemplate = {
      question: domanda,
      answer: risposta,
    };

    try {
      await deleteTemplate(selectedTemplateId);

      await saveTemplate(nuovoTemplate);

      const updatedTemplates = await fetchTemplateList();
      setTemplates(updatedTemplates);

      setModificaOpen(false);
      setSelectedTemplateId(null);
    } catch (error) {
      console.error('Errore durante la modifica del template:', error);
      alert('Errore durante la modifica del template.');
    }
  };

  const apriDialogModifica = (templateId) => {
    setSelectedTemplateId(templateId);
    setModificaOpen(true);
  };


  useEffect(() => {
    const fetchTemplates = async () => {
      try {
        const data = await fetchTemplateList();
        setTemplates(data);
      } catch (error) {
        console.error('Errore durante il fetch dei template:', error);
      }
    };

    fetchTemplates();
  }, []);

  return (
    <>
      <div className='all'>
        <h1 style={{ paddingBottom: '5px', borderBottom: '1px solid grey' }}>Gestione Templates</h1>

        <div className="btnsTop">
          <Button startIcon={<AddBoxIcon />} style={buttons} onClick={apriDialogAggiuntaTemplate}>Aggiungi template</Button>
        </div>

        { }
        {templates.map((template, index) => (
          <Accordion key={template.id} className='template' style={backTemplate}>
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls={`panel${index}-content`}
              id={`panel${index}-header`}
            >
              <Typography component="span" style={{ fontSize: '22px', fontWeight: '600' }}>
                {template.question.length > 30
                  ? `${template.question.substring(0, 30)}...`
                  : template.question}
              </Typography>
            </AccordionSummary>
            <AccordionDetails className='contenuto'>
              <div className="domanda">
                <h3>Domanda:</h3>
                <p>{template.question}</p>
              </div>
              <div className="domanda">
                <h3>Risposta:</h3>
                <p>{template.answer}</p>
              </div>
            </AccordionDetails>
            <AccordionActions>
              <Tooltip title='Modifica Template' placement='top'>
                <Button style={buttons} onClick={() => apriDialogModifica(template.id)}>
                  <EditIcon />
                </Button>
              </Tooltip>
              <Tooltip title='Elimina Template' placement='top'>
                <Button
                  style={buttons}
                  onClick={() => apriDialogEliminazione(template.id)}
                >
                  <DeleteForeverIcon />
                </Button>
              </Tooltip>
            </AccordionActions>
          </Accordion>
        ))}
      </div>

      { }
      <Dialog open={AggiuntaTemplate} onClose={chiudiDialogAggiuntaTemplate} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '30px', margin: '16px 24px 0 24px', fontWeight: 'bold', }, ...textStyle }}>Aggiunta Template</DialogContentText>
        <DialogContentText style={{ ...{ fontSize: '16px', marginLeft: '24px', }, ...textStyle }}>Completa i campi seguenti per aggiungere il nuovo Template</DialogContentText>
        <DialogContent>
          <TextField style={{ ...{ borderRadius: '8px', marginTop: '20px', }, ...inputChatStyle }}
            placeholder="Domanda"
            fullWidth
            required
          />
          <textarea
            id="description"
            name="description"
            required
            rows="5"
            placeholder='Risposta'
            style={{ ...{ marginTop: '20px', }, ...inputChatStyle }}
          />
        </DialogContent>
        <DialogActions style={{ marginBottom: '25px', marginRight: '24px' }}>
          <Button onClick={chiudiDialogAggiuntaTemplate} style={buttons}>Annulla</Button>
          <Button onClick={AggiungiTemplate} style={buttons}>Aggiungi Template</Button>
        </DialogActions>
      </Dialog>

      { }
      <Dialog open={Modifica} onClose={chiudiDialogModifica} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...textStyle }}>
          Modifica Template
        </DialogContentText>
        <DialogContentText style={{ ...{ fontSize: '16px', margin: '6px 24px 0 24px', }, ...textStyle }}>
          Modifica i campi seguenti per aggiornare il Template
        </DialogContentText>
        <DialogContent style={{ paddingTop: '10px', paddingBottom: '10px' }}>
          <TextField style={{ ...{ borderRadius: '8px' }, ...inputChatStyle }}
            placeholder="Domanda"
            fullWidth
            required
          />
          <textarea
            id="description"
            name="description"
            required
            rows="5"
            placeholder='Risposta'
            style={{ ...{ marginTop: '20px', }, ...inputChatStyle }}
          />
        </DialogContent>
        <DialogActions style={{ marginBottom: '20px', marginRight: '24px' }}>
          <Button onClick={chiudiDialogModifica} style={buttons}>Annulla</Button>
          <Button onClick={ModificaTemplate} style={buttons}>Modifica</Button>
        </DialogActions>
      </Dialog>

      { }
      <Dialog open={Eliminazione} onClose={chiudiDialogEliminazione}>
        <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...textStyle }}>
          {`Eliminare il template con ID: ${selectedTemplateId}?`}
        </DialogContentText>
        <DialogContentText style={{ ...{ fontSize: '16px', margin: '6px 24px 0 24px', }, ...textStyle }}>
          Sei sicuro di voler eliminare questo Template? Questa azione non può essere annullata.
        </DialogContentText>
        <DialogActions style={{ margin: '10px 16px 20px 0' }}>
          <Button onClick={chiudiDialogEliminazione} style={buttons}>Annulla</Button>
          <Button onClick={handleDeleteTemplate} style={buttons}>Elimina Template</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default Templates;
