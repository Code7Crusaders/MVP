import pytest
from flask import Flask, json
from app.main import app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_chat_valid_input(client):
    """Test /api/chat_interact with valid input."""
    """

    curl -X POST http://localhost:5000/api/chat_interact \
     -H "Content-Type: application/json" \
     -d '{"user": "123", "question": "Ciao chi sei e come puoi aiutarmi?"}'

    """

    response = client.post("/api/chat_interact", json={"user": "123", "question": "Ciao chi sei e come puoi aiutarmi?"})

    assert response.status_code == 200

    data = response.get_json()  
    assert "answer" in data  
    assert data["answer"] is not None

    print(data["answer"])
