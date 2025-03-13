from flask import Flask, request, jsonify
from app.controllers.chat_controller import ChatController

app = Flask(__name__)

# Initialize the controller
chat_controller = ChatController()

@app.route("/", methods=["GET"])
def home():
    """
    Root route that returns a simple welcome message.
    """
    return jsonify({"message": "Welcome to the Flask API!"}), 200

@app.route("/api/get_messages", methods=["POST"])
def get_messages():
    """
    Route to get messages from the ChatController.
    """
    data = request.get_json()

    if not data or "quantity" not in data:
        return jsonify({"status": "error", "message": "Invalid request body"}), 400

    quantity = data["quantity"]
    
    # Call the controller's method to get messages
    messages = chat_controller.get_messages(quantity)

    return jsonify(messages), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
