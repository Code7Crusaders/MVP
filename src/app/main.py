from flask import Flask, request, jsonify
import os
import fitz

from dependencies.encoding import detect_encoding
from dependencies.dependency_inj import dependency_injection

from dto.AnswerDTO import AnswerDTO
from dto.QuestionDTO import QuestionDTO
from dto.FileDTO import FileDTO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")  
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

app = Flask(__name__)

# Initialize dependencies
dependencies = dependency_injection()
chat_controller = dependencies["chat_controller"]
add_file_controller = dependencies["add_file_controller"]

@app.route("/api/add_file", methods=["POST"])
def add_file():
    """Endpoint to upload a PDF or TXT file.

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
def chat():
    """Chat endpoint to receive a question and return an answer.

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
