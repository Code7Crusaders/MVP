```bash
# Build the Docker image
docker build -t flask-backend .

# Run the Docker container
docker run -p 5000:5000 flask-backend
```