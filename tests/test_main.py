import json
import pytest # type: ignore
from app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_chat_valid_input(client):
    response = client.post("/chat", data=json.dumps({
        "user": "123",
        "question": "Which beers are available?"
    }), content_type='application/json')
    assert response.status_code == 200
    assert "answer" in response.get_json()

def test_chat_invalid_input_missing_user(client):
    response = client.post("/chat", data=json.dumps({
        "question": "Which beers are available?"
    }), content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid input"}

def test_chat_invalid_input_missing_question(client):
    response = client.post("/chat", data=json.dumps({
        "user": "123"
    }), content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid input"}

def test_chat_invalid_json(client):
    response = client.post("/chat", data="Invalid JSON", content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid input"}
    

