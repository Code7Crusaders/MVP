import unittest
from unittest.mock import patch, MagicMock
import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="eddy1234",
            host="localhost",
            port="5432"
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        execute_query(connection, create_table_query)