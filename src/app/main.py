from flask import Flask, request, jsonify

from app.dto.AnswerDTO import AnswerDTO
from app.dto.QuestionDTO import QuestionDTO
from app.controllers.chat_controller import ChatController
from app.services.chat_service import ChatService
from app.services.similarity_search_service import SimilaritySearchService
from app.services.generate_answer_service import GenerateAnswerService
from app.adapters.faiss_adapter import FaissAdapter
# from app.adapters.langChain_adapter import LangChainAdapter
from app.repositories.faiss_repository import FaissRepository

app = Flask(__name__)

# Initialize 
faiss_repository = FaissRepository()
faiss_adapter = FaissAdapter(faiss_repository)

generate_answer_service = GenerateAnswerService()

similarity_search_service = SimilaritySearchService(faiss_adapter)
chat_service = ChatService(similarity_search_service, generate_answer_service)
chat_controller = ChatController(chat_service)

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
