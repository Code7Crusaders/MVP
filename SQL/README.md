# PostgreSQL Docker Setup

## Build the Docker Image
To build the Docker image, run the following command:

```bash
docker build -t my-postgres-db .
```

## Run the Docker Container
To run the container, use the command below:

```bash
docker run -d -p 5432:5432 --env-file .env --name postgres-container my-postgres-db
```

- `-d`: Runs the container in detached mode.
- `-p 5432:5432`: Maps port 5432 on the host to port 5432 in the container.
- `--env-file .env`: Specifies the environment variables file.
- `--name postgres-container`: Assigns a name to the container.

Make sure you have a `.env` file in the same directory with the required environment variables.