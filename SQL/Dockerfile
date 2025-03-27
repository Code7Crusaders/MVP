# Use the official PostgreSQL image
FROM postgres:latest

# Copy the SQL script to the initialization directory
COPY db.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

# Start PostgreSQL
CMD ["postgres"]