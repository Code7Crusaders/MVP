from flask import Flask, request, jsonify

from app.dto.AnswerDTO import AnswerDTO
from app.dto.QuestionDTO import QuestionDTO
from app.controllers.chat_controller import ChatController

app = Flask(__name__)

# Initialize the controller
chat_controller = ChatController()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    question = QuestionDTO(data["user"], data["question"])

    try:
        return jsonify(chat_controller.get_answer(question)), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
