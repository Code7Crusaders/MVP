```bash
# Build the Docker image
docker build -t flask-backend .

# Run the Docker container
docker run -p 5001:5001 flask-backend
```