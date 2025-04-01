import React, { useState } from "react";
import '../css/Documenti.css';
import { useTheme } from "@emotion/react";
import { Button, CircularProgress } from "@mui/material"; // Importa CircularProgress
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { styled } from "@mui/material";
import AddCircleIcon from '@mui/icons-material/AddCircle';
import Alert from '@mui/material/Alert';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import Collapse from '@mui/material/Collapse';
import { uploadFile } from "../utils/api"; 

function Documenti() {
    const theme = useTheme();

    const [fileName, setFileName] = useState("Nessuno");
    const [selectedFile, setSelectedFile] = useState(null); 
    const [alertVisible, setAlertVisible] = useState(false);
    const [open, setOpen] = React.useState(true);
    const [uploadSuccess, setUploadSuccess] = useState(false); 
    const [uploadError, setUploadError] = useState(""); 
    const [isUploading, setIsUploading] = useState(false); 

    const inputChatStyle = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgba(17, 25, 40, 0.9)' : '#ededed',
        color: theme.palette.mode === 'dark' ? 'white' : 'black',
    };

    const buttons = {
        backgroundColor: theme.palette.mode === 'dark' ? 'rgb(233, 233, 233)' : '#333',
        color: theme.palette.mode === 'dark' ? '#333' : 'white',
    };

    const textStyle = {
        color: theme.palette.mode === 'dark' ? 'white' : 'black',
    };

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

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile) {
            const fileExtension = selectedFile.name.split('.').pop().toLowerCase();
            if (fileExtension === 'txt' || fileExtension === 'pdf') {
                setFileName(selectedFile.name);
                setSelectedFile(selectedFile); 
                setAlertVisible(false);
            } else {
                setFileName("Nessuno");
                setSelectedFile(null); 
                setAlertVisible(true);
                setOpen(true);
            }
        } else {
            setFileName("Nessuno");
            setSelectedFile(null);
            setAlertVisible(false);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            setUploadError("Nessun file selezionato per il caricamento.");
            return;
        }

        setIsUploading(true); 
        setUploadSuccess(false);
        setUploadError("");

        try {
            const response = await uploadFile(selectedFile);
            console.log("File caricato con successo:", response);
            setUploadSuccess(true);
        } catch (error) {
            console.error("Errore durante il caricamento del file:", error);
            setUploadError(error.message || "Errore sconosciuto durante il caricamento.");
        } finally {
            setIsUploading(false); 
        }
    };

    return (
        <div className="all">
            <h1 style={{ paddingBottom: '5px', borderBottom: '1px solid grey' }}>Aggiungi documento</h1>

            {alertVisible && (
                <Collapse in={open}>
                    <Alert
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
                        Formato non supportato! I file caricati devono essere in formato '.pdf' o '.txt'
                    </Alert>
                </Collapse>
            )}

            {uploadSuccess && (
                <Alert severity="success" sx={{ mb: 2 }}>
                    File caricato con successo!
                </Alert>
            )}

            {uploadError && (
                <Alert severity="error" sx={{ mb: 2 }}>
                    {uploadError}
                </Alert>
            )}

            <div className="uploadBox" style={inputChatStyle}>
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
                        onChange={handleFileChange}
                        multiple={false}
                    />
                </Button>

                <div className="File">
                    <p>File selezionato: </p>
                    <span style={textStyle}> &nbsp;&nbsp;'{fileName}'</span>
                </div>
            </div>

            <div style={{ marginTop: '20px', textAlign: 'center' }}>
                {isUploading && <CircularProgress />} {}
            </div>

            <Button
                startIcon={<AddCircleIcon />}
                className="btnBottom"
                style={buttons}
                onClick={handleUpload} 
                disabled={isUploading} 
            >
                Aggiungi Documento
            </Button>
        </div>
    );
}

export default Documenti;
