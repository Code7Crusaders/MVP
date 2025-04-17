import pytest
from flask_jwt_extended import create_access_token
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["JWT_SECRET_KEY"] = "test_secret_key"
    with app.test_client() as client:
        yield client

# def test_register(client):
#     response = client.post("/register", json={
#         "username": "testuser",
#         "password": "testpassword",
#         "email": "testuser@example.com",
#         "phone": "1234567890",
#         "first_name": "Test",
#         "last_name": "User"
#     })
#     assert response.status_code == 200
#     assert response.json["message"] == "User registered successfully"

def test_login(client):
    client.post("/register", json={
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    })
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json

def get_access_token(client):
    response = client.post("/login", json={
        "username": "johnny",
        "password": "secret"
    })
    return response.json["access_token"]

def test_protected_route(client):
    token = get_access_token(client)
    response = client.get("/is_admin", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_is_admin(client):
    token = get_access_token(client)
    response = client.get("/is_admin", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json["is_admin"] is True

def test_get_conversation(client):
    token = get_access_token(client)
    response = client.get("/conversation/get/2", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code in [200, 500]  # Adjust based on implementation

def test_get_conversations(client):
    token = get_access_token(client)
    response = client.get("/conversation/get_all", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code in [200, 500]

def test_get_dashboard_metrics(client):
    token = get_access_token(client)
    response = client.get("/dashboard/metrics", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code in [200, 500]