from flask import Flask, request, jsonify

from app.dto.AnswerDTO import AnswerDTO
from app.dto.QuestionDTO import QuestionDTO
from app.controllers.chat_controller import ChatController

app = Flask(__name__)

# Initialize the controller
chat_controller = ChatController()

@app.route("/chat", methods=["POST"])
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
        return jsonify({"answer": answer.get_answer()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(400)
def bad_request(error):
    response = jsonify({"error": "Invalid input"})
    response.status_code = 400
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
