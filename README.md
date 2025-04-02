# Readme

---

## Code Coverage

![Coverage](coverage.svg)

[View Full Coverage Report](htmlcov/index.html)

## Project Overview

This project is a Flask-based web application that provides API endpoints for handling chat-related functionalities. It is designed to be lightweight, easy to set up, and extendable.

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

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Create and Activate a Virtual Environment

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Running the Flask App

```bash
python src/app/main.py
```

The app will be accessible at `http://127.0.0.1:5001`.

### 5. Running Tests

To run the test suite:

```bash
pytest tests/
```

This will execute the test cases in `tests/test_routes.py`.

### 6. Checking Test Coverage

To measure the test coverage, use the following command:

```bash
pytest --cov=src/app
```

This will generate a report showing the coverage percentage of the application code.

## API Endpoints

### **1. GET /**

**Description:** Returns a simple welcome message.

**Response:**
```json
{
  "message": "Welcome to the Flask API!"
}
```

### **2. POST /api/get_messages**

**Description:** Accepts a `quantity` parameter in the request body and returns a list of dummy messages.

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

To run the application using Docker:

```bash
docker-compose up --build
```

This will build the Docker images and start the containers as defined in the `docker-compose.yml` file. The application will be accessible at `http://127.0.0.1:5001`.

## Test Coverage

To ensure code quality, this project includes test coverage analysis. To generate a test coverage report:

```bash
pytest --cov=src/app --cov-report=html
```

This will create an `htmlcov` directory containing a visual report of the test coverage, which can be opened in a browser.

