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
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import styled from '@mui/material/styles/styled';
import AddBoxIcon from '@mui/icons-material/AddBox';
import { AccordionActions, Tooltip } from '@mui/material';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import MapsUgcIcon from '@mui/icons-material/MapsUgc';
import { useState } from 'react';
import { Dialog, DialogContent, DialogActions, TextField, DialogContentText, Alert } from '@mui/material';


function Templates() {
    const [AggiuntaTemplate, setAggTemplateOpen] = useState(false); // Stato per gestire il DIALOG dell'aggiunta di un Template
    const [Modifica, setModificaOpen] = useState(false); // Stato per gestire il DIALOG della modifica di una domanda
    const [AggiuntaDomanda, setAggDomandaOpen] = useState(false); // Stato per gestire il DIALOG dell'aggiunta di una domanda
    const [Eliminazione, setEliminazioneOpen] = useState(false); // Stato per gestire il DIALOG dell'eliminazione

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
        '&::placeholder': {
          color: theme.palette.mode === 'dark' ? 'lightgray' : 'gray',} 
    }

    const VisuallyHiddenInput = styled('input')({
        clip: 'rect(0 0 0 0)',
        clipPath: 'inset(50%)',
        height: 1,
        overflow: 'hidden',
        position: 'absolute',
        bottom: 0,
        left: 0,
        whiteSpace: 'nowrap',
        width: 1,
      });

    // DIALOG per l'aggiunta di un Template
    const chiudiDialogAggiuntaTemplate = () => {
        setAggTemplateOpen(false); 
    };
    const AggiungiTemplate = () => {
        //controllare che non sia vuoto
        // Aggiunta Template
        setAggTemplateOpen(false); 
    };
    const apriDialogAggiuntaTemplate = () => {
        setAggTemplateOpen(true); 
    };

    // DIALOG per la modifica di una domanda
    const chiudiDialogModifica = () => {
        setModificaOpen(false); 
    };
    const ModificaDomanda = () => {
        //controllare che non sia vuota
        // Modifica domanda
        setModificaOpen(false); 
    };
    const apriDialogModifica = () => {
        setModificaOpen(true); 
    };

    // DIALOG per l'aggiunta di una domanda
    const chiudiDialogAggiuntaDomanda = () => {
        setAggDomandaOpen(false); 
    };
    const AggiungiDomanda = () => {
        //controllare che non sia vuota
        // Aggiunta domanda
        setAggDomandaOpen(false); 
    };
    const apriDialogAggiuntaDomanda = () => {
        setAggDomandaOpen(true); 
    };


    // DIALOG per l'eliminazione del Template
    const chiudiDialogEliminazione = () => {
        setEliminazioneOpen(false); 
    };
    const EliminaTemplate = () => {
        // Eliminazione del Template
        setEliminazioneOpen(false); 
    };
    const apriDialogEliminazione = () => {
        setEliminazioneOpen(true); 
    };

  return (
    <>
    <div className='all'>
    <h1 style={{paddingBottom: '5px', borderBottom: '1px solid grey'}}>Gestione Templates</h1>

    <div className="btnsTop">
        <Button startIcon={<AddBoxIcon />} style={buttons} onClick={apriDialogAggiuntaTemplate}>Aggiungi template</Button>
        <Button
            style={buttons}
            component="label"
            role={undefined}
            variant="contained"
            tabIndex={-1}
            startIcon={<CloudUploadIcon />}
        >   
        Upload files
        <VisuallyHiddenInput
            type="file"
            onChange={(event) => console.log(event.target.files)}
            multiple
        />
        </Button>
    </div>


    <Accordion className='template' style={backTemplate}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1-content"
          id="panel1-header"
        >
          <Typography component="span" style={{fontSize: '20px', fontWeight: '550'}}>Template 1</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di un'altra domanda nello stesso template?</p>
            </div>
        </AccordionDetails>
        <AccordionActions>
            <Tooltip title='Aggiungi domanda' placement='top'><Button style={buttons} onClick={apriDialogAggiuntaDomanda}><MapsUgcIcon /></Button></Tooltip>
            <Tooltip title='Elimina Template' placement='top'><Button style={buttons} onClick={apriDialogEliminazione}><DeleteForeverIcon /></Button></Tooltip>
        </AccordionActions>
      </Accordion>
      <Accordion className='template' style={backTemplate}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1-content"
          id="panel1-header"
        >
          <Typography component="span" style={{fontSize: '20px', fontWeight: '550'}}>Template 2</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di un'altra domanda nello stesso template?</p>
            </div>
        </AccordionDetails>
      </Accordion>
      <Accordion className='template' style={backTemplate}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1-content"
          id="panel1-header"
        >
          <Typography component="span" style={{fontSize: '20px', fontWeight: '550'}}>Template 3</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons} onClick={apriDialogModifica}><EditIcon /></button>
                </div>
                <p>Prova di un'altra domanda nello stesso template?</p>
            </div>
        </AccordionDetails>
      </Accordion> 
    </div>

    {/* DIALOG per l'aggiunta di un Template */}
    <Dialog open={AggiuntaTemplate} onClose={chiudiDialogAggiuntaTemplate} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '30px', margin: '16px 24px 0 24px', fontWeight: 'bold', }, ...textStyle }}>Aggiunta Template</DialogContentText>
        <DialogContentText style={{...{fontSize: '16px', marginLeft:'24px',}, ...textStyle }}>Inserisci il nome del Template</DialogContentText>
        <DialogContent>
          <TextField style={{ ...{borderRadius: '8px'}, ...inputChatStyle}}
            placeholder="Nome Template"
            fullWidth
          />
        </DialogContent>
        <DialogActions style={{marginBottom: '25px', marginRight: '24px'}}>
          <Button onClick={chiudiDialogAggiuntaTemplate} style={buttons}>Annulla</Button>
          <Button onClick={AggiungiTemplate} style={buttons}>Aggiungi</Button>
        </DialogActions>
    </Dialog>

    {/* DIALOG per la modifica di una domanda */}
    <Dialog open={Modifica} onClose={chiudiDialogModifica} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '20px', margin: '20px 24px 0 24px', fontWeight: '500', }, ...textStyle }}>Modifica domanda</DialogContentText>
        <DialogContent style={{paddingTop: '10px', paddingBottom: '10px'}}>
          <TextField style={{ ...{borderRadius: '8px'}, ...inputChatStyle}}
            placeholder="Domanda"
            fullWidth
          />
        </DialogContent>
        <DialogActions style={{marginBottom: '20px', marginRight: '24px'}}>
          <Button onClick={chiudiDialogModifica} style={buttons}>Annulla</Button>
          <Button onClick={ModificaDomanda} style={buttons}>Modifica</Button>
        </DialogActions>
    </Dialog>

    {/* DIALOG per l'aggiunta di una domanda */}
    <Dialog open={AggiuntaDomanda} onClose={chiudiDialogAggiuntaDomanda} fullWidth>
        <DialogContentText style={{ ...{ fontSize: '30px', margin: '16px 24px 0 24px', fontWeight: 'bold', }, ...textStyle }}>Template n</DialogContentText>
        <DialogContentText style={{...{fontSize: '16px', marginLeft:'24px',}, ...textStyle }}>Inserisci la domanda da aggiungere</DialogContentText>
        <DialogContent>
          <TextField style={{ ...{borderRadius: '8px'}, ...inputChatStyle}}
            placeholder="Domanda"
            fullWidth
          />
        </DialogContent>
        <DialogActions style={{marginBottom: '25px', marginRight: '24px'}}>
          <Button onClick={chiudiDialogAggiuntaDomanda} style={buttons}>Annulla</Button>
          <Button onClick={AggiungiDomanda} style={buttons}>Aggiungi</Button>
        </DialogActions>
    </Dialog>

    {/* DIALOG per l'eliminazione della chat */}
    <Dialog open={Eliminazione} onClose={chiudiDialogEliminazione}>
      <DialogContentText style={{ ...{ fontSize: '20px', margin: '16px 24px 0 24px', fontWeight: 'bold', borderBottom: '0.8px solid', paddingBottom: '6px' }, ...textStyle }}>Template n</DialogContentText>
      <DialogContentText style={{ ...{ fontSize: '16px', margin:'6px 24px 0 24px',}, ...textStyle }}>Sei sicuro di voler eliminare questo Template?</DialogContentText>
        <DialogActions style={{margin: '10px 16px 20px 0'}}>
          <Button onClick={chiudiDialogEliminazione} style={buttons}>Annulla</Button>
          <Button onClick={EliminaTemplate} style={buttons}>Elimina Template</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default Templates;
