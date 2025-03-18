import pytest
from flask import Flask, json
from app.main import app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_chat_valid_input(client, mocker):
    """Test /api/chat_interact with valid input."""
    mock_response = mocker.Mock()
    mock_response.get_answer.return_value = "This is a test answer."
    mocker.patch("app.main.chat_controller.get_answer", return_value=mock_response)

    response = client.post("/api/chat_interact", json={"user": "123", "question": "What is AI?"})
    
    assert response.status_code == 200
    data = response.get_json()
    assert "answer" in data
    assert data["answer"] == "This is a test answer."

def test_chat_missing_fields(client):
    """Test /api/chat_interact with missing fields."""
    response = client.post("/api/chat_interact", json={"user": "123"}) 
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Invalid input"

    response = client.post("/api/chat_interact", json={"question": "What is AI?"})  
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Invalid input"

    response = client.post("/api/chat_interact", json={})  
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Invalid input"

