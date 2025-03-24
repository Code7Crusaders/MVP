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

function Templates() {

    const theme = useTheme();
      
    const backTemplate = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgb(0, 9, 28)' : '#ededed',
        color: theme.palette.mode === 'dark' ? 'white' : 'black',
      };

    const buttons = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
        color: theme.palette.mode === 'dark' ? '#333' : 'white', 
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

  return (
    <>
    <div className='all'>
    <h1 style={{paddingBottom: '5px', borderBottom: '1px solid grey'}}>Gestione Templates</h1>

    <div className="btnsTop">
        <Button startIcon={<AddBoxIcon />} style={buttons}>Aggiungi template</Button>
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
                    <button style={buttons}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons}><EditIcon /></button>
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
          <Typography component="span" style={{fontSize: '20px', fontWeight: '550'}}>Template 2</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons}><EditIcon /></button>
                </div>
                <p>Prova di una domanda di un template?</p>
            </div>
            <div className="domanda">
                <div className="actions">
                    <button style={buttons}><DeleteIcon /></button>
                    <button style={buttons}><EditIcon /></button>
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
                    <button style={buttons}><EditIcon /></button>
                </div>
                <p>Prova di un'altra domanda nello stesso template?</p>
            </div>
        </AccordionDetails>
      </Accordion> 
    </div>
    </>
  );
}

export default Templates;
