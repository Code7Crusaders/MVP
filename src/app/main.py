from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

import os
import fitz
import pytz
from datetime import datetime

from utils.midleware_admin import admin_required

from dependencies.encoding import detect_encoding
from dependencies.dependency_inj import dependency_injection

from dto.answer_dto import AnswerDTO
from dto.question_dto import QuestionDTO
from dto.file_dto import FileDTO
from dto.conversation_dto import ConversationDTO
from dto.message_dto import MessageDTO
from dto.support_message_dto import SupportMessageDTO
from dto.template_dto import TemplateDTO
from dto.user_dto import UserDTO


italy_tz = pytz.timezone('Europe/Rome')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")  
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

app = Flask(__name__)

# Initialize dependencies
dependencies = dependency_injection(app)

chat_controller = dependencies["chat_controller"]
add_file_controller = dependencies["add_file_controller"]

get_conversation_controller = dependencies["get_conversation_controller"]
get_conversations_controller = dependencies["get_conversations_controller"]
save_conversation_title_controller = dependencies["save_conversation_title_controller"]

get_message_controller = dependencies["get_message_controller"]
get_messages_by_conversation_controller = dependencies["get_messages_by_conversation_controller"]
save_message_controller = dependencies["save_message_controller"]

get_support_message_controller = dependencies["get_support_message_controller"]
get_support_messages_controller = dependencies["get_support_messages_controller"]
save_support_message_controller = dependencies["save_support_message_controller"]

delete_template_controller = dependencies["delete_template_controller"]
get_template_controller = dependencies["get_template_controller"]
get_template_list_controller = dependencies["get_template_list_controller"]
save_template_controller = dependencies["save_template_controller"]

registration_controller = dependencies["registration_controller"]
authentication_controller = dependencies["authentication_controller"]

# ---- Authentication Routes ----

@app.route("/register", methods=["POST"])
def register():
    """
    curl -X POST http://127.0.0.1:5000/register \
    -H "Content-Type: application/json" \
    -d '{"username": "john", "password": "secret", "email": "john@example.com", "phone": "1234567890", "first_name": "John", "last_name": "Doe"}'
    """
    try:
        data = request.json

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        phone = data.get("phone", "")
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")

        user_dto = UserDTO(
            username=username,
            password=password,
            email=email,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            is_admin=False
        )

        registration_controller.register(user_dto)

        return jsonify({"message": "User registered successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/login", methods=["POST"])
def login():
    """
    curl -X POST http://127.0.0.1:5000/login \
    -H "Content-Type: application/json" \
    -d '{"username": "john", "password": "secret"}'
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user_dto = UserDTO(
            username=username,
            password=password
        )

        user_result = authentication_controller.login(user_dto)    

        access_token = create_access_token(identity=str(user_result.get_id()), additional_claims={"is_admin": user_result.get_is_admin()})

        return jsonify(access_token=access_token), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---- Conversation Routes ----
@app.route("/conversation/get/<int:conversation_id>", methods=["GET"])
@jwt_required()
def get_conversation(conversation_id):
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/conversation/get/<conversation_id> \
    -H "Authorization: Bearer <your_token>"
    
    """
    conversation = ConversationDTO(
        id=conversation_id
    )

    try:
        conversation_result = get_conversation_controller.get_conversation(conversation)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "id": conversation_result.get_id(),
        "title": conversation_result.get_title()
    }), 200


@app.route("/conversation/get_all", methods=["GET"])
@jwt_required()
def get_conversations():
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/conversation/get_all \
    -H "Authorization: Bearer <your_token>"
    """

    try:
        conversations = get_conversations_controller.get_conversations()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify([{
        "id": conversation.get_id(),
        "title": conversation.get_title()
    } for conversation in conversations]), 200


@app.route("/conversation/save_title", methods=["POST"])
@jwt_required()
def save_conversation_title():
    """
    # To test this endpoint with curl:
    curl -X POST http://127.0.0.1:5000/conversation/save_title -H "Content-Type: application/json" -d '{"title": "New Conversation Title"}' \
    -H "Authorization: Bearer <your_token>"
    """
    data = request.get_json()

    conversation = ConversationDTO(
        title=data.get("title")
    )

    try:
        saved_id = save_conversation_title_controller.save_conversation_title(conversation)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": f"Conversation title saved with id: {saved_id}"}), 200


# ---- Message Routes ----
@app.route("/message/get/<int:message_id>", methods=["GET"])
@jwt_required()
def get_message(message_id):
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/message/get/<message_id> \
    -H "Authorization: Bearer <your_token>"
    """

    message = MessageDTO(
        id=message_id
    )

    try:
        message_result = get_message_controller.get_message(message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "id": message_result.get_id(),
        "text": message_result.get_text(),
        "user_id": message_result.get_user_id(),
        "conversation_id": message_result.get_conversation_id(),
        "rating": message_result.get_rating(),
        "created_at": message_result.get_created_at()
    }), 200


@app.route("/message/get_by_conversation/<int:conversation_id>", methods=["GET"])
@jwt_required()
def get_messages_by_conversation(conversation_id):
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/message/get_by_conversation/<conversation_id> \
    -H "Authorization: Bearer <your_token>"
    """

    message = MessageDTO(
        conversation_id=conversation_id
    )

    try:
        messages_result = get_messages_by_conversation_controller.get_messages_by_conversation(message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    jsonify([{
        "id": message.get_id(),
        "text": message.get_text(),
        "user_id": message.get_user_id(),
        "conversation_id": message.get_conversation_id(),
        "rating": message.get_rating(),
        "created_at": message.get_created_at()
    } for message in messages_result]), 200


@app.route("/message/save", methods=["POST"])
@jwt_required()
def save_message():
    """
    # To test this endpoint with curl:
    curl -X POST http://127.0.0.1:5000/message/save \
    -H "Content-Type: application/json" \
    -d '{"text": "Message text", "user_id": 1, "conversation_id": 2, "rating": true}' \
    -H "Authorization: Bearer <your_token>"
    """
    data = request.get_json()

    # Create DTO
    message = MessageDTO(
        text=data.get("text"),
        user_id=data.get("user_id"),
        conversation_id=data.get("conversation_id"),
        rating=data.get("rating"),
        created_at=datetime.now(italy_tz)
    )

    try:
        saved_id = save_message_controller.save_message(message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": f"Message saved with id: {saved_id}"}), 200


# ---- Support Message Routes ----
@app.route("/support_message/get/<int:support_message_id>", methods=["GET"])
@jwt_required()
def get_support_message(support_message_id):
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/support_message/get/<support_message_id> \
    -H "Authorization: Bearer <your_token>"
    """

    support_message_dto = SupportMessageDTO(
        id=support_message_id
    )

    try:
        support_message = get_support_message_controller.get_support_message(support_message_dto)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({
        "id": support_message.get_id(),
        "user_id": support_message.get_user_id(),
        "description": support_message.get_description(),
        "status": support_message.get_status(),
        "subject": support_message.get_subject(),
        "created_at": support_message.get_created_at()
        }), 200


@app.route("/support_message/get_all", methods=["GET"])
@jwt_required()
def get_support_messages():
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/support_message/get_all \
    -H "Authorization: Bearer <your_token>"
    """
    try:
        support_messages = get_support_messages_controller.get_support_messages()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify([{
        "id": message.get_id(),
        "user_id": message.get_user_id(),
        "description": message.get_description(),
        "status": message.get_status(),
        "subject": message.get_subject(),
        "created_at": message.get_created_at()
    } for message in support_messages]), 200


@app.route("/support_message/save", methods=["POST"])
@jwt_required()
def save_support_message():
    """
    # To test this endpoint with curl:
    curl -X POST http://127.0.0.1:5000/support_message/save \
    -H "Content-Type: application/json" \
    -d '{"user_id": 1, "description": "Support message description", "status": "true", "subject": "Support subject"}' \
    -H "Authorization: Bearer <your_token>"
    """
    data = request.get_json()

    # Create DTO
    support_message = SupportMessageDTO(
        user_id=data.get("user_id"),
        description=data.get("description"),
        status=data.get("status"),
        subject=data.get("subject"),
        created_at=datetime.now(italy_tz)
    )

    try:
        saved_id = save_support_message_controller.save_support_message(support_message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": f"Support message saved with id: {saved_id}"}), 200


# ---- Template Routes ----
@app.route("/template/delete/<int:template_id>", methods=["DELETE"])
@admin_required
def delete_template(template_id):
    """
    # To test this endpoint with curl:
    curl -X DELETE http://127.0.0.1:5000/template/delete/<template_id> \
    -H "Authorization: Bearer <your_token>"
    """
    template_dto = TemplateDTO(
        id=template_id
    )

    try:
        result = delete_template_controller.delete_template(template_dto)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if result:
        return jsonify({"message": f"Template with id {template_id} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Failed to delete template with id {template_id}"}), 500


@app.route("/template/get/<int:template_id>", methods=["GET"])
@jwt_required()
def get_template(template_id):
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/template/get/<template_id> \
    -H "Authorization: Bearer <your_token>"
    """

    template_dto = TemplateDTO(
        id=template_id
    )

    try:
        template = get_template_controller.get_template(template_dto)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "id": template.get_id(),
        "question": template.get_question(),
        "answer": template.get_answer(),
        "author_id": template.get_author_id(),
        "last_modified": template.get_last_modified()
    }), 200


@app.route("/template/get_list", methods=["GET"])
@jwt_required()
def get_template_list():
    """
    # To test this endpoint with curl:
    curl -X GET http://127.0.0.1:5000/template/get_list \
    -H "Authorization: Bearer <your_token>"
    """
    try:
        templates = get_template_list_controller.get_template_list()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify([{
        "id": template.get_id(),
        "question": template.get_question(),
        "answer": template.get_answer(),
        "author_id": template.get_author_id(),
        "last_modified": template.get_last_modified()
    } for template in templates]), 200


@app.route("/template/save", methods=["POST"])
@admin_required
def save_template():
    """
    # To test this endpoint with curl:
    curl -X POST http://127.0.0.1:5000/template/save \
    -H "Content-Type: application/json" \
    -d '{"question": "Sample question", "answer": "Sample answer", "author_id": 1}' \
    -H "Authorization: Bearer <your_token>"
    """
    data = request.get_json()

    # Create DTO
    template = TemplateDTO(
        question=data.get("question"),
        answer=data.get("answer"),
        author_id=data.get("author_id"),
        last_modified=datetime.now(italy_tz)
    )

    try:
        saved_id = save_template_controller.save_template(template)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": f"Template saved with id: {saved_id}"}), 200


@app.route("/api/add_file", methods=["POST"])
@jwt_required()
def add_file():
    """Endpoint to upload a PDF or TXT file.
    curl -X POST http://127.0.0.1:5000/api/add_file \
    -H "Authorization: Bearer <your_token>" \
    -F "file=@/path/to/your/file.pdf"


    API Call:
    - Method: POST
    - URL: /api/add_file
    - Request Body (multipart/form-data):
      - "file": the file to upload (must be PDF or TXT)

    Possible Responses:
    - 200 OK: {"message": "File successfully uploaded"}
    - 400 Bad Request: {"error": "No file part"} (if no file is provided)
    - 400 Bad Request: {"error": "No selected file"} (if the file is not selected)
    - 400 Bad Request: {"error": "Unsupported file type"} (if the file is not a PDF or TXT)
    - 400 Bad Request: {"error": "File encoding not supported. Please use UTF-8."} (if a TXT file has unsupported encoding)
    - 400 Bad Request: {"error": "Error reading PDF: <details>"} (if there is an issue reading the PDF)
    
    Functionality:
    - Checks if a file was uploaded correctly.
    - Validates the file extension (.pdf or .txt).
    - Saves the file in UPLOAD_FOLDER. (optional)
    - Reads the file content and passes it to the controller via a DTO.
    """

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # verify file type
    if not (file.filename.endswith('.pdf') or file.filename.endswith('.txt')):
        return jsonify({"error": "Unsupported file type"}), 400

    # save file 
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Read file content
    if file.filename.endswith('.txt'):
        file_encoding = detect_encoding(file_path)
        try:
            with open(file_path, 'r', encoding=file_encoding) as f:
                file_content = f.read()
        except UnicodeDecodeError:
            return jsonify({"error": "File encoding not supported. Please use UTF-8."}), 400
    
    elif file.filename.endswith('.pdf'):
        try:
            doc = fitz.open(file_path)
            file_content = "\n".join([page.get_text() for page in doc])
        except Exception as e:
            return jsonify({"error": f"Error reading PDF: {str(e)}"}), 400

    # DTO and controller
    file_dto = FileDTO(file.filename, file_content)
    add_file_controller.load_file(file_dto)

    return jsonify({"message": "File successfully uploaded"}), 200


@app.route("/api/chat_interact", methods=["POST"])
@jwt_required()
def chat():
    """Chat endpoint to receive a question and return an answer.
    curl -X POST http://localhost:5000/api/chat_interact \
    -H "Content-Type: application/json" \
    -d '{"user": "123", "question": "Potresti consigliarmi degli alimenti a base di latticini di cui possiendi informazioni?"}' \
    -H "Authorization: Bearer <your_token>"
    
    API Call:
    - Method: POST
    - URL: /api/chat_interact
    - Request Body (JSON):
      {
          "user": "User ID",
          "question": "Question text"
      }

    Possible Responses:
    - 200 OK: {"answer": "Generated assistant response"}
    - 400 Bad Request: {"error": "Invalid input"} (if required fields are missing)
    - 500 Internal Server Error: {"error": "<error message>"} (if an internal error occurs)

    Functionality:
    - Validates that the request JSON contains "user" and "question" fields.
    - Creates a DTO with the user input.
    - Calls the controller to generate a response.
    - Returns the generated answer or an error in case of issues.
    
    """
    data = request.get_json()

    # Validate input
    if "user" not in data or "question" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = data["user"]
    question = data["question"]

    # Create DTO and get response
    user_input = QuestionDTO(user_id, question)
    answer = chat_controller.get_answer(user_input)

    try:
        return jsonify({"answer": answer.get_answer()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(400) 
def bad_request(error):
    response = jsonify({"error": "Invalid input"})
    response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
