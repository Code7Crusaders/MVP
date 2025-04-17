# Readme


🎥 Video preview of the MVP

[![Guarda il video](https://img.youtube.com/vi/Dq2FcwWGRtU/maxresdefault.jpg)](https://youtu.be/Dq2FcwWGRtU)

## Code Coverage

![Coverage](coverage.svg)

[View Full Coverage Report](https://code7crusaders.github.io/MVP/)

## Project Overview

This project is a React Flask-based web application that provides API endpoints for handling chat-related functionalities. It is designed to be lightweight, easy to set up, and extendable.

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

