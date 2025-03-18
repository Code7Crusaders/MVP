import pytest
from io import BytesIO
from unittest.mock import patch, MagicMock
from app.main import app, add_file_controller, detect_encoding
from app.controllers.add_file_controller import AddFileController

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.main.detect_encoding", return_value="utf-8")
@patch.object(add_file_controller, "load_file")
def test_upload_txt_file(mock_load_file, mock_detect_encoding, client):
    mock_load_file.return_value = None
    
    data = {
        "file": (BytesIO(b"Sample text content"), "test.txt")
    }
    response = client.post("/api/add_file", content_type='multipart/form-data', data=data)
    
    assert response.status_code == 200
    assert "File successfully uploaded" in response.get_json()["message"]
    mock_load_file.assert_called_once()

@patch.object(add_file_controller, "load_file")
def test_upload_pdf_file(mock_load_file, client):
    mock_load_file.return_value = None
    
    pdf_mock = MagicMock()
    pdf_mock.get_text.return_value = "PDF content"
    with patch("fitz.open", return_value=[pdf_mock]):
        data = {
            "file": (BytesIO(b"%PDF-1.4"), "test.pdf")
        }
        response = client.post("/api/add_file", content_type='multipart/form-data', data=data)
        
        assert response.status_code == 200
        assert "File successfully uploaded" in response.get_json()["message"]
        mock_load_file.assert_called_once()

def test_upload_no_file(client):
    response = client.post("/api/add_file", content_type='multipart/form-data', data={})
    assert response.status_code == 400
    assert "No file part" in response.get_json()["error"]

def test_upload_unsupported_file_type(client):
    data = {
        "file": (BytesIO(b"Some content"), "image.jpg")
    }
    response = client.post("/api/add_file", content_type='multipart/form-data', data=data)
    assert response.status_code == 400
    assert "Unsupported file type" in response.get_json()["error"]