import json
import pytest
from app.main import app


# # Test the /api/get_messages route (POST)
# def test_get_messages():
#     client = app.test_client()

#     # Valid request
#     response = client.post(
#         "/api/get_messages",
#         json={"quantity": 3}
#     )
#     data = json.loads(response.data)

#     assert response.status_code == 200
#     assert len(data) == 3
#     assert data[0]["id"] == 0
#     assert data[1]["text"] == "Message 1"

#     # Invalid request (missing 'quantity')
#     response = client.post(
#         "/api/get_messages",
#         json={}
#     )
#     data = json.loads(response.data)

#     assert response.status_code == 400
#     assert data["status"] == "error"
#     assert data["message"] == "Invalid request body"
