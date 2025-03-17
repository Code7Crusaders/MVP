import psycopg2
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# from adapters.postgres_adapter import PostgresAdapter
# from repositories.postgres_repository import PostgresRepository

from controllers.add_file_controller import AddFileController
from controllers.chat_controller import ChatController

from services.chat_service import ChatService
from services.similarity_search_service import SimilaritySearchService
from services.generate_answer_service import GenerateAnswerService
from services.add_file_service import AddFileService
from services.split_file_service import SplitFileService
from services.add_chunks_service import AddChunksService

from adapters.faiss_adapter import FaissAdapter
from adapters.langChain_adapter import LangChainAdapter

from repositories.faiss_repository import FaissRepository
from repositories.langChain_repository import LangChainRepository

from models.prompt_template_model import PromptTemplateModel

load_dotenv()


# def initialize_postgres() -> PostgresAdapter:
#     """
#     Initializes and returns an instance of PostgresAdapter.
#     Configures the connection to the Postgres database using the credentials specified in the environment variables.
#     Returns:
#       - PostgresAdapter: An instance of PostgresAdapter.
#     Raises:
#       - Exception: If an error occurs during Postgres initialization.
#     """
#     try:
#         db_config = {
#             "host": os.getenv("DB_HOST", "localhost"),
#             "port": os.getenv("DB_PORT", "5432"),
#             "user": os.getenv("DB_USER", "postgres"),
#             "password": os.getenv("DB_PASSWORD", "eddy1234"),
#             "dbname": os.getenv("DB_NAME", "postgres")
#         }
#         conn = psycopg2.connect(
#             host=db_config["host"],
#             port=db_config["port"],
#             user=db_config["user"],
#             password=db_config["password"],
#             dbname=db_config["dbname"]
#         )
#         # Creazione delle tabelle necessarie
#         with conn.cursor() as cursor:
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS messages (
#             id SERIAL PRIMARY KEY,
#             content TEXT,
#             timestamp TIMESTAMP,
#             sender VARCHAR(50)
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS loading_attempts (
#             id SERIAL PRIMARY KEY,
#             starting_timestamp TIMESTAMP,
#             ending_timestamp TIMESTAMP,
#             outcome BOOLEAN
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS platform_logs (
#             id SERIAL PRIMARY KEY,
#             loading_attempt_id INTEGER REFERENCES loading_attempts(id),
#             loading_item VARCHAR(50),
#             timestamp TIMESTAMP,
#             outcome BOOLEAN
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS vector_store_logs (
#             id SERIAL PRIMARY KEY,
#             loading_attempt_id INTEGER REFERENCES loading_attempts(id),
#             timestamp TIMESTAMP,
#             outcome BOOLEAN,
#             num_added_items INTEGER,
#             num_modified_items INTEGER,
#             num_deleted_items INTEGER
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Users (
#             id SERIAL PRIMARY KEY,
#             username VARCHAR(256) NOT NULL UNIQUE,
#             password_hash VARCHAR NOT NULL,
#             email VARCHAR NOT NULL UNIQUE,
#             phone CHAR(16),
#             first_name VARCHAR NOT NULL,
#             last_name VARCHAR NOT NULL,
#             is_admin BOOLEAN DEFAULT FALSE
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Conversations (
#             id SERIAL PRIMARY KEY,
#             title VARCHAR NOT NULL
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS User_Messages (
#             id SERIAL PRIMARY KEY,
#             text VARCHAR NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             user_id INTEGER NOT NULL,
#             conversation_id INTEGER NOT NULL,
#             FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
#             FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Bot_Messages (
#             id SERIAL PRIMARY KEY,
#             text VARCHAR NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             rating BOOLEAN,
#             conversation_id INTEGER NOT NULL,
#             FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Support (
#             id SERIAL PRIMARY KEY,
#             user_id INTEGER NOT NULL,
#             description VARCHAR NOT NULL,
#             status BOOLEAN DEFAULT FALSE,
#             subject VARCHAR NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Templates (
#             id SERIAL PRIMARY KEY,
#             question VARCHAR NOT NULL,
#             answer VARCHAR NOT NULL,
#             author VARCHAR NOT NULL,
#             last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             FOREIGN KEY (author) REFERENCES Users(username) ON DELETE CASCADE
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Products (
#             id SERIAL PRIMARY KEY,
#             country_of_origin VARCHAR NOT NULL,
#             weight INTEGER,
#             milk_type VARCHAR,
#             description VARCHAR,
#             manufacturer VARCHAR,
#             product_name VARCHAR NOT NULL,
#             image BYTEA
#             );
#             """)
#             cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Message_Products (
#             message_id INTEGER NOT NULL,
#             product_id INTEGER NOT NULL,
#             PRIMARY KEY (message_id, product_id),
#             FOREIGN KEY (message_id) REFERENCES User_Messages(id) ON DELETE CASCADE,
#             FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
#             );
#             """)
#         conn.commit()

#         postgres_repository = PostgresRepository(conn)
#         postgres_adapter = PostgresAdapter(postgres_repository)
#         return postgres_adapter
#     except psycopg2.Error as e:
#         raise Exception(f"Error connecting to Postgres: {e}")
    
def initialize_langchain() -> LangChainAdapter:

    # Read API key from .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    model = ChatOpenAI(
        model="gpt-4o-mini", 
        max_tokens=2000, 
        temperature=0.5, 
        request_timeout=10
    )

    langchain_repository = LangChainRepository(model)
    langchain_adapter = LangChainAdapter(langchain_repository)

    return langchain_adapter

    

def initialize_faiss() -> FaissAdapter:

    # Read API key from .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    # OpenAI embedding model
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)

    vector_store = FAISS.from_texts([""], embedding_model)

    faiss_repository = FaissRepository(vector_store)
    faiss_adapter = FaissAdapter(faiss_repository)

    return faiss_adapter

def initialize_prompt_template() -> PromptTemplateModel:

    template = "Sei un assistente virtuale esperto, progettato per fornire risposte precise, " \
    "esaustive e professionali riguardanti l'azienda Valsana. Rispondi alle domande in italiano con un tono professionale, " \
    "ma accessibile e amichevole, e fai riferimento alle informazioni fornite dall'azienda."

    return PromptTemplateModel(template)

def dependency_injection() -> dict[str, object]:
    """
    Initializes and returns a dictionary of controllers dependencies.
    Returns:
      - dict[str, object]: A dictionary of controllers dependencies.
    """

    # Postgres

    

    # Initialize 
    langchain_adapter = initialize_langchain()
    faiss_adapter = initialize_faiss() 
    prompt_template = initialize_prompt_template()
    

    # Langchain
    generate_answer_service = GenerateAnswerService(langchain_adapter, prompt_template)
    split_file_service = SplitFileService(langchain_adapter)

    # Faiss
    similarity_search_service = SimilaritySearchService(faiss_adapter)
    add_chunks_service = AddChunksService(faiss_adapter)

    # Chat Service
    add_file_service = AddFileService(split_file_service, add_chunks_service)
    chat_service = ChatService(similarity_search_service, generate_answer_service)


    # Controllers
    add_file_controller = AddFileController(add_file_service)
    chat_controller = ChatController(chat_service)

    dependencies = {
        "chat_controller": chat_controller,
        "add_file_controller": add_file_controller
    }

    return dependencies

if __name__ == "__main__":
    try:
        postgres_adapter = initialize_postgres()
        print("Postgres initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize Postgres: {e}")
