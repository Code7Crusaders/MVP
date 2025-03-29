import psycopg2
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_bcrypt import Bcrypt
from datetime import timedelta

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

from dependencies.init_vector_store import VECTOR_STORE_PATH, load_vector_store
from config.db_config import db_config

from controllers.add_file_controller import AddFileController
from controllers.chat_controller import ChatController
from controllers.delete_template_controller import DeleteTemplateController
from controllers.get_conversation_controller import GetConversationController
from controllers.get_conversations_controller import GetConversationsController
from controllers.get_message_controller import GetMessageController
from controllers.get_messages_by_conversation_controller import GetMessagesByConversationController
from controllers.get_support_message_controller import GetSupportMessageController
from controllers.get_support_messages_controller import GetSupportMessagesController
from controllers.get_template_controller import GetTemplateController
from controllers.get_template_list_controller import GetTemplateListController
from controllers.save_conversation_title_controller import SaveConversationTitleController
from controllers.delete_conversation_controller import DeleteConversationController
from controllers.save_message_controller import SaveMessageController
from controllers.update_message_rating_controller import UpdateMessageRatingController
from controllers.save_support_message_controller import SaveSupportMessageController
from controllers.save_template_controller import SaveTemplateController
from controllers.registration_controller import RegistrationController
from controllers.authentication_controller import AuthenticationController

from services.chat_service import ChatService
from services.similarity_search_service import SimilaritySearchService
from services.generate_answer_service import GenerateAnswerService
from services.add_file_service import AddFileService
from services.split_file_service import SplitFileService
from services.add_chunks_service import AddChunksService
from services.delete_template_service import DeleteTemplateService
from services.get_conversation_service import GetConversationService
from services.get_conversations_service import GetConversationsService
from services.get_message_service import GetMessageService
from services.get_messages_by_conversation_service import GetMessagesByConversationService 
from services.get_support_message_service import GetSupportMessageService
from services.get_support_messages_service import GetSupportMessagesService
from services.get_template_list_service import GetTemplateListService
from services.get_template_service import GetTemplateService
from services.save_conversation_title_service import SaveConversationTitleService
from services.delete_conversation_service import DeleteConversationService
from services.save_message_service import SaveMessageService
from services.update_message_rating_service import UpdateMessageRatingService
from services.save_support_message_service import SaveSupportMessageService
from services.save_template_service import SaveTemplateService 
from services.registration_service import RegistrationService
from services.validation_service import ValidationService
from services.authentication_service import AuthenticationService

from adapters.faiss_adapter import FaissAdapter
from adapters.langChain_adapter import LangChainAdapter
from adapters.conversation_postgres_adapter import ConversationPostgresAdapter
from adapters.message_postgres_adapter import MessagePostgresAdapter
from adapters.support_message_postgres_adapter import  SupportMessagePostgresAdapter 
from adapters.template_postgres_adapter import TemplatePostgresAdapter
from adapters.user_postgres_adapter import UserPostgresAdapter

from repositories.faiss_repository import FaissRepository
from repositories.langChain_repository import LangChainRepository
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from repositories.message_postgres_repository import MessagePostgresRepository
from repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from repositories.template_postgres_repository import TemplatePostgresRepository
from repositories.user_postgres_repository import UserPostgresRepository

from models.prompt_template_model import PromptTemplateModel

load_dotenv()


def initialize_postgres():
    """
    """
    try:

        conn = psycopg2.connect(**db_config)
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(256) NOT NULL UNIQUE,
                password_hash VARCHAR(512) NOT NULL,
                email VARCHAR(256) NOT NULL UNIQUE,
                phone CHAR(16),
                first_name VARCHAR(256) NOT NULL,
                last_name VARCHAR(256) NOT NULL,
                is_admin BOOLEAN DEFAULT FALSE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Conversations (
                id SERIAL PRIMARY KEY,
                title VARCHAR(256) NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Messages (
                id SERIAL PRIMARY KEY,
                text VARCHAR(1024) NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER,
                conversation_id INTEGER NOT NULL,
                rating BOOLEAN,
                FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
                FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Support (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                description VARCHAR(1024) NOT NULL,
                status BOOLEAN DEFAULT FALSE,
                subject VARCHAR(256) NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Templates (
                id SERIAL PRIMARY KEY,
                question VARCHAR(1024) NOT NULL,
                answer VARCHAR(1024) NOT NULL,
                author INTEGER NOT NULL,
                last_modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author) REFERENCES Users(id) ON DELETE CASCADE
            );
            """)
        conn.commit()

    except psycopg2.Error as e:
        raise Exception(f"Error connecting to Postgres: {e}")
    
def initialize_langchain() -> LangChainAdapter:
    try:
        # Read API key from .env
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        model = ChatOpenAI(
            model="gpt-4o-mini", 
            max_tokens=2000, 
            temperature=0.5, 
            request_timeout=15
        )

        langchain_repository = LangChainRepository(model)
        langchain_adapter = LangChainAdapter(langchain_repository)

        return langchain_adapter

    except Exception as e:
        raise Exception(f"Error initializing LangChain: {e}")


def initialize_faiss() -> FaissAdapter:
    try:
        # Read API key from .env
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        # OpenAI embedding model
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)

        if os.path.exists(VECTOR_STORE_PATH) and os.listdir(VECTOR_STORE_PATH):
            vector_store = load_vector_store(embedding_model)
        else:
            vector_store = FAISS.from_texts([""], embedding_model)

        faiss_repository = FaissRepository(vector_store)
        faiss_adapter = FaissAdapter(faiss_repository)

        return faiss_adapter

    except Exception as e:
        raise Exception(f"Error initializing FAISS: {e}")

def initialize_prompt_template() -> PromptTemplateModel:
    try:
        # Define the prompt template for the virtual assistant
        template = "Sei un assistente virtuale esperto, progettato per fornire risposte precise, " \
                   "esaustive e professionali riguardanti l'azienda Valsana. Rispondi alle domande in italiano con un tono professionale, " \
                   "ma accessibile e amichevole, e fai riferimento alle informazioni fornite dall'azienda."

        return PromptTemplateModel(template)
    except Exception as e:
        raise Exception(f"Error initializing prompt template: {e}")


def initialize_conversation_postgres() -> ConversationPostgresAdapter:
    try:
        # Initialize the repository and adapter for conversation-related operations
        conversation_postgres_repository = ConversationPostgresRepository(db_config)

        return ConversationPostgresAdapter(conversation_postgres_repository)
    except Exception as e:
        raise Exception(f"Error initializing conversation Postgres adapter: {e}")


def initialize_message_postgres() -> MessagePostgresAdapter:
    try:
        # Initialize the repository and adapter for message-related operations
        message_postgres_repository = MessagePostgresRepository(db_config)

        return MessagePostgresAdapter(message_postgres_repository)
    except Exception as e:
        raise Exception(f"Error initializing message Postgres adapter: {e}")


def initialize_support_message_postgres() -> SupportMessagePostgresAdapter:
    try:
        # Initialize the repository and adapter for support message-related operations
        support_message_postgres_repository = SupportMessagePostgresRepository(db_config)

        return SupportMessagePostgresAdapter(support_message_postgres_repository)
    except Exception as e:
        raise Exception(f"Error initializing support message Postgres adapter: {e}")


def initialize_template_postgres() -> TemplatePostgresAdapter:
    try:
        # Initialize the repository and adapter for template-related operations
        template_postgres_repository = TemplatePostgresRepository(db_config)

        return TemplatePostgresAdapter(template_postgres_repository)
    except Exception as e:
        raise Exception(f"Error initializing template Postgres adapter: {e}")
    
def initialize_user_postgres() -> UserPostgresAdapter:
    try:
        # Initialize the repository and adapter for user-related operations
        user_postgres_repository = UserPostgresRepository(db_config)

        return UserPostgresAdapter(user_postgres_repository)
    except Exception as e:
        raise Exception(f"Error initializing user Postgres adapter: {e}")


def dependency_injection(app : Flask) -> dict[str, object]:
    """
    Initializes and returns a dictionary of controllers dependencies.
    Returns:
      - dict[str, object]: A dictionary of controllers dependencies.
    """
    try:

        # Secure Secret Key
        app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)  # Token expires in 30 min

        jwt = JWTManager(app)
        bcrypt = Bcrypt(app)

        # Initialize Postgres
        initialize_postgres()

        # Initialize 
        prompt_template = initialize_prompt_template()

        # Adapter
        langchain_adapter = initialize_langchain()
        faiss_adapter = initialize_faiss() 
            
        # Postgres
        conversation_postgres_adapter = initialize_conversation_postgres()
        message_postgres_adapter = initialize_message_postgres()
        support_message_postgres_adapter = initialize_support_message_postgres()
        template_postgres_adapter = initialize_template_postgres()
        user_postgres_adapter = initialize_user_postgres()
        
        # Services
        # Langchain
        generate_answer_service = GenerateAnswerService(langchain_adapter, prompt_template)
        split_file_service = SplitFileService(langchain_adapter)

        # Faiss
        similarity_search_service = SimilaritySearchService(faiss_adapter)
        add_chunks_service = AddChunksService(faiss_adapter)

        # Chat Service
        add_file_service = AddFileService(split_file_service, add_chunks_service)
        chat_service = ChatService(similarity_search_service, generate_answer_service)

        # Postgres
        get_conversation_service = GetConversationService(conversation_postgres_adapter)
        get_conversations_service = GetConversationsService(conversation_postgres_adapter)
        save_conversation_title_service = SaveConversationTitleService(conversation_postgres_adapter)
        delete_conversation_service = DeleteConversationService(conversation_postgres_adapter)

        get_message_service = GetMessageService(message_postgres_adapter)
        get_messages_by_conversation_service = GetMessagesByConversationService(message_postgres_adapter) 
        save_message_service = SaveMessageService(message_postgres_adapter)
        update_message_rating_service = UpdateMessageRatingService(message_postgres_adapter)

        get_support_message_service = GetSupportMessageService(support_message_postgres_adapter)
        get_support_messages_service = GetSupportMessagesService(support_message_postgres_adapter)
        save_support_message_service = SaveSupportMessageService(support_message_postgres_adapter)

        delete_template_service = DeleteTemplateService(template_postgres_adapter)
        get_template_service = GetTemplateService(template_postgres_adapter)
        get_template_list_service = GetTemplateListService(template_postgres_adapter)
        save_template_service = SaveTemplateService(template_postgres_adapter) 

        validation_service = ValidationService(user_postgres_adapter)
        registration_service = RegistrationService(user_postgres_adapter, validation_service, bcrypt)
        authentication_service = AuthenticationService(user_postgres_adapter, bcrypt)
        

        # Controllers
        add_file_controller = AddFileController(add_file_service)
        chat_controller = ChatController(chat_service)

        get_conversation_controller = GetConversationController(get_conversation_service)
        get_conversations_controller = GetConversationsController(get_conversations_service)
        save_conversation_title_controller = SaveConversationTitleController(save_conversation_title_service)

        get_message_controller = GetMessageController(get_message_service)
        get_messages_by_conversation_controller = GetMessagesByConversationController(get_messages_by_conversation_service)
        save_message_controller = SaveMessageController(save_message_service)
        delete_conversation_controller = DeleteConversationController(delete_conversation_service)

        get_support_message_controller = GetSupportMessageController(get_support_message_service)
        get_support_messages_controller = GetSupportMessagesController(get_support_messages_service)
        save_support_message_controller = SaveSupportMessageController(save_support_message_service)
        update_message_rating_controller = UpdateMessageRatingController(update_message_rating_service)

        delete_template_controller = DeleteTemplateController(delete_template_service)
        get_template_controller = GetTemplateController(get_template_service)
        get_template_list_controller = GetTemplateListController(get_template_list_service)
        save_template_controller = SaveTemplateController(save_template_service)

        registration_controller = RegistrationController(registration_service)
        authentication_controller = AuthenticationController(authentication_service)

        dependencies = {
            "chat_controller": chat_controller,
            "add_file_controller": add_file_controller,
            "get_conversation_controller": get_conversation_controller,
            "get_conversations_controller": get_conversations_controller,
            "save_conversation_title_controller": save_conversation_title_controller,
            "get_message_controller": get_message_controller,
            "get_messages_by_conversation_controller": get_messages_by_conversation_controller,
            "save_message_controller": save_message_controller,
            "update_message_rating_controller": update_message_rating_controller,
            "get_support_message_controller": get_support_message_controller,
            "get_support_messages_controller": get_support_messages_controller,
            "save_support_message_controller": save_support_message_controller,
            "delete_template_controller": delete_template_controller,
            "get_template_controller": get_template_controller,
            "get_template_list_controller": get_template_list_controller,
            "save_template_controller": save_template_controller,
            "registration_controller": registration_controller,
            "authentication_controller": authentication_controller,
            "delete_conversation_controller": delete_conversation_controller
        }

        return dependencies

    except Exception as e:
        raise Exception(f"Error during dependency injection: {e}")

