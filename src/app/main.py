from flask import Flask, request, jsonify

from dependencies.dependency_inj import dependency_injection

from dto.AnswerDTO import AnswerDTO
from dto.QuestionDTO import QuestionDTO
from dto.FileDTO import FileDTO


app = Flask(__name__)

# Initialize dependencies
dependencies = dependency_injection()
chat_controller = dependencies["chat_controller"]
add_file_controller = dependencies["add_file_controller"]


@app.route("/api/add_file", methods=["POST"])
def add_file():
    """Endpoint to add a PDF or TXT file."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and (file.filename.endswith('.pdf') or file.filename.endswith('.txt')):
        # file_path = f"/upload/{file.filename}"
        # file.save(file_path)

        # Read file content
        file_content = file.read()

        # Assuming you have a FileDTO class and add_file_controller
        file_dto = FileDTO(file.filename, file_content)

        # Process the file (your controller method)
        add_file_controller.load_file(file_dto)

        return jsonify({"message": "File successfully uploaded"}), 200
    else:
        return jsonify({"error": "Unsupported file type"}), 400


@app.route("/api/chat_interact", methods=["POST"])
def chat():
    """Chat endpoint to receive a question and return an answer."""
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
