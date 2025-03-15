import psycopg2
import os

from app.adapters.postgres_adapter import PostgresAdapter
from app.repositories.postgres_repository import PostgresRepository
from app.controllers.chat_controller import ChatController
from app.services.chat_service import ChatService
from app.services.similarity_search_service import SimilaritySearchService
from app.services.generate_answer_service import GenerateAnswerService
from app.adapters.faiss_adapter import FaissAdapter
from app.adapters.langChain_adapter import LangChainAdapter
from app.repositories.faiss_repository import FaissRepository
from app.repositories.langChain_repository import LangChainRepository


def initialize_postgres() -> PostgresAdapter:
    """
    Initializes and returns an instance of PostgresAdapter.
    Configures the connection to the Postgres database using the credentials specified in the environment variables.
    Returns:
      - PostgresAdapter: An instance of PostgresAdapter.
    Raises:
      - Exception: If an error occurs during Postgres initialization.
    """
    try:
        db_config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432"),
            "user": os.getenv("DB_USER", "postgres"),
            "password": os.getenv("DB_PASSWORD", "eddy1234"),
            "dbname": os.getenv("DB_NAME", "postgres")
        }
        conn = psycopg2.connect(
            host=db_config["host"],
            port=db_config["port"],
            user=db_config["user"],
            password=db_config["password"],
            dbname=db_config["dbname"]
        )
        # Creazione delle tabelle necessarie
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT,
            timestamp TIMESTAMP,
            sender VARCHAR(50)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS loading_attempts (
            id SERIAL PRIMARY KEY,
            starting_timestamp TIMESTAMP,
            ending_timestamp TIMESTAMP,
            outcome BOOLEAN
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS platform_logs (
            id SERIAL PRIMARY KEY,
            loading_attempt_id INTEGER REFERENCES loading_attempts(id),
            loading_item VARCHAR(50),
            timestamp TIMESTAMP,
            outcome BOOLEAN
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS vector_store_logs (
            id SERIAL PRIMARY KEY,
            loading_attempt_id INTEGER REFERENCES loading_attempts(id),
            timestamp TIMESTAMP,
            outcome BOOLEAN,
            num_added_items INTEGER,
            num_modified_items INTEGER,
            num_deleted_items INTEGER
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(256) NOT NULL UNIQUE,
            password_hash VARCHAR NOT NULL,
            email VARCHAR NOT NULL UNIQUE,
            phone CHAR(16),
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            is_admin BOOLEAN DEFAULT FALSE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Conversations (
            id SERIAL PRIMARY KEY,
            title VARCHAR NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS User_Messages (
            id SERIAL PRIMARY KEY,
            text VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER NOT NULL,
            conversation_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
            FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Bot_Messages (
            id SERIAL PRIMARY KEY,
            text VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            rating BOOLEAN,
            conversation_id INTEGER NOT NULL,
            FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Support (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            description VARCHAR NOT NULL,
            status BOOLEAN DEFAULT FALSE,
            subject VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Templates (
            id SERIAL PRIMARY KEY,
            question VARCHAR NOT NULL,
            answer VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author) REFERENCES Users(username) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
            id SERIAL PRIMARY KEY,
            country_of_origin VARCHAR NOT NULL,
            weight INTEGER,
            milk_type VARCHAR,
            description VARCHAR,
            manufacturer VARCHAR,
            product_name VARCHAR NOT NULL,
            image BYTEA
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Message_Products (
            message_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            PRIMARY KEY (message_id, product_id),
            FOREIGN KEY (message_id) REFERENCES User_Messages(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
            );
            """)
        conn.commit()

        postgres_repository = PostgresRepository(conn)
        postgres_adapter = PostgresAdapter(postgres_repository)
        return postgres_adapter
    except psycopg2.Error as e:
        raise Exception(f"Error connecting to Postgres: {e}")
    
def initialize_langchain() -> LangChainAdapter:

    langchain_repository = LangChainRepository()
    langchain_adapter = LangChainAdapter(langchain_repository)

    return langchain_adapter

    

def initialize_faiss() -> FaissAdapter:

    faiss_repository = FaissRepository()
    faiss_adapter = FaissAdapter(faiss_repository)

    return faiss_adapter


def dependency_injection() -> dict[str, object]:
    """
    Initializes and returns a dictionary of controllers dependencies.
    Returns:
      - dict[str, object]: A dictionary of controllers dependencies.
    """

    # Postgres

    # Langchain

    # Initialize 
    langchain_adapter = initialize_langchain()
    generate_answer_service = GenerateAnswerService(langchain_adapter)

    # Faiss
    faiss_adapter = initialize_faiss()    
    similarity_search_service = SimilaritySearchService(faiss_adapter)

    # Chat Service
    chat_service = ChatService(similarity_search_service, generate_answer_service)


    # Controllers

    chat_controller = ChatController(chat_service)

    dependencies = {
        "chat_controller": chat_controller
    }

    return dependencies

if __name__ == "__main__":
    try:
        postgres_adapter = initialize_postgres()
        print("Postgres initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize Postgres: {e}")
