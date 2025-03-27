# Use the official Python image as the base image
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Copy the .env file from the parent directory to the container
COPY .env /app/.env

# Set the Python path
ENV PYTHONPATH=/app

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app/main.py"]
