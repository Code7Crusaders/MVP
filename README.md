# Readme
---

## Project Structure

```
src/
│── app/
│   ├── main.py               # Main Flask app
│   ├── controllers/
│   │   ├── chat_controller.py # Controller for chat-related logic
tests/
├── test_routes.py            # Tests for routes
```

## Setup Instructions

1. **Clone the repository**

    Clone this repository to your local machine.

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Create and activate a virtual environment**

    If you don't have a virtual environment yet, create one:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. **Install dependencies**

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Here, the `requirements.txt` file should include dependencies like Flask and pytest. Example:

    ```ini
    Flask==2.2.2
    pytest==8.3.5
    ```

4. **Running the Flask App**

    To start the Flask app, run the following command:

    ```bash
    python src/app/main.py
    ```

    The app will run at `http://127.0.0.1:5001`. You can test it by visiting this URL in your browser or using an API client like Postman or cURL.

5. **Running Tests**

    To ensure everything is working, run the tests using pytest:

    ```bash
    pytest tests/
    ```

    This will run the tests in `tests/test_routes.py` and ensure both the `/` and `/api/get_messages` routes are functioning properly.

## Endpoints

1. **GET /**

    **Description:** Returns a simple welcome message.

    **Response:**

    ```json
    {
      "message": "Welcome to the Flask API!"
    }
    ```

2. **POST /api/get_messages**

    **Description:** Accepts a `quantity` parameter in the request body and returns a list of dummy messages based on the quantity.

    **Request (JSON body):**

    ```json
    {
      "quantity": 3
    }
    ```

    **Response:**

    ```json
    [
      {"id": 0, "text": "Message 0"},
      {"id": 1, "text": "Message 1"},
      {"id": 2, "text": "Message 2"}
    ]
    ```

    **Error Response (if no quantity is provided):**

    ```json
    {
      "status": "error",
      "message": "Invalid request body"
    }
    ```
    ## Running with Docker

    To run the application using Docker, ensure you have Docker and Docker Compose installed on your system. Then, execute the following command:

    ```bash
    docker-compose up --build
    ```

    This will build the Docker images and start the containers as defined in the `docker-compose.yml` file. Once the containers are running, the Flask app will be accessible at `http://127.0.0.1:5001`.