import pytest
from unittest.mock import MagicMock, patch
from flask import Flask
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from adapters.langChain_adapter import LangChainAdapter
from adapters.faiss_adapter import FaissAdapter
from models.prompt_template_model import PromptTemplateModel
from psycopg2 import connect

from dependencies.dependency_inj import (
    initialize_postgres,
    initialize_langchain,
    initialize_faiss,
    initialize_prompt_template,
    initialize_conversation_postgres,
    initialize_message_postgres,
    initialize_support_message_postgres,
    initialize_template_postgres,
    initialize_user_postgres,
    dependency_injection,
)


@pytest.fixture
def mock_app():
    return Flask(__name__)


def test_initialize_postgres_success():
    with patch("dependencies.dependency_inj.psycopg2.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        # Act
        initialize_postgres()

        # Assert
        mock_connect.assert_called_once()
        mock_conn.commit.assert_called_once()


def test_initialize_postgres_failure():
    with patch("dependencies.dependency_inj.psycopg2.connect", side_effect=Exception("Connection failed")):
        with pytest.raises(Exception, match="Connection failed"):
            initialize_postgres()


def test_initialize_langchain_success():
    with patch("dependencies.dependency_inj.ChatOpenAI") as mock_chat_openai:
        mock_model = MagicMock()
        mock_chat_openai.return_value = mock_model

        result = initialize_langchain()

        assert isinstance(result, LangChainAdapter)
        mock_chat_openai.assert_called_once()


def test_initialize_langchain_failure():
    with patch("dependencies.dependency_inj.ChatOpenAI", side_effect=Exception("LangChain init failed")):
        with pytest.raises(Exception, match="Error initializing LangChain: LangChain init failed"):
            initialize_langchain()


def test_initialize_faiss_success():
    with patch("dependencies.dependency_inj.OpenAIEmbeddings") as mock_embeddings:
        with patch("dependencies.dependency_inj.FAISS.from_texts") as mock_faiss_from_texts:
            mock_embedding_model = MagicMock()
            mock_embeddings.return_value = mock_embedding_model
            mock_vector_store = MagicMock()
            mock_faiss_from_texts.return_value = mock_vector_store

            result = initialize_faiss()

            assert isinstance(result, FaissAdapter)
            mock_embeddings.assert_called_once()


def test_initialize_faiss_failure():
    with patch("dependencies.dependency_inj.OpenAIEmbeddings", side_effect=Exception("FAISS init failed")):
        with pytest.raises(Exception, match="Error initializing FAISS: FAISS init failed"):
            initialize_faiss()


def test_initialize_prompt_template_success():
    result = initialize_prompt_template()
    assert isinstance(result, PromptTemplateModel)


def test_initialize_prompt_template_failure():
    with patch("dependencies.dependency_inj.PromptTemplateModel", side_effect=Exception("Prompt init failed")):
        with pytest.raises(Exception, match="Error initializing prompt template: Prompt init failed"):
            initialize_prompt_template()


def test_initialize_conversation_postgres_success():
    with patch("dependencies.dependency_inj.ConversationPostgresRepository") as mock_repo:
        mock_adapter = initialize_conversation_postgres()
        assert mock_repo.called
        assert mock_adapter is not None


def test_initialize_message_postgres_success():
    with patch("dependencies.dependency_inj.MessagePostgresRepository") as mock_repo:
        mock_adapter = initialize_message_postgres()
        assert mock_repo.called
        assert mock_adapter is not None


def test_initialize_support_message_postgres_success():
    with patch("dependencies.dependency_inj.SupportMessagePostgresRepository") as mock_repo:
        mock_adapter = initialize_support_message_postgres()
        assert mock_repo.called
        assert mock_adapter is not None


def test_initialize_template_postgres_success():
    with patch("dependencies.dependency_inj.TemplatePostgresRepository") as mock_repo:
        mock_adapter = initialize_template_postgres()
        assert mock_repo.called
        assert mock_adapter is not None


def test_initialize_user_postgres_success():
    with patch("dependencies.dependency_inj.UserPostgresRepository") as mock_repo:
        mock_adapter = initialize_user_postgres()
        assert mock_repo.called
        assert mock_adapter is not None


def test_dependency_injection_success(mock_app):
    with patch("dependencies.dependency_inj.initialize_postgres") as mock_init_postgres, \
         patch("dependencies.dependency_inj.initialize_langchain") as mock_init_langchain, \
         patch("dependencies.dependency_inj.initialize_faiss") as mock_init_faiss, \
         patch("dependencies.dependency_inj.initialize_prompt_template") as mock_init_prompt_template, \
         patch("dependencies.dependency_inj.initialize_conversation_postgres") as mock_init_conversation, \
         patch("dependencies.dependency_inj.initialize_message_postgres") as mock_init_message, \
         patch("dependencies.dependency_inj.initialize_support_message_postgres") as mock_init_support, \
         patch("dependencies.dependency_inj.initialize_template_postgres") as mock_init_template, \
         patch("dependencies.dependency_inj.initialize_user_postgres") as mock_init_user:

        dependencies = dependency_injection(mock_app)

        assert "chat_controller" in dependencies
        assert "add_file_controller" in dependencies
        assert "get_conversation_controller" in dependencies
        assert "get_conversations_controller" in dependencies
        assert "save_conversation_title_controller" in dependencies
        assert "get_message_controller" in dependencies
        assert "get_messages_by_conversation_controller" in dependencies
        assert "save_message_controller" in dependencies
        assert "update_message_rating_controller" in dependencies
        assert "get_support_message_controller" in dependencies
        assert "get_support_messages_controller" in dependencies
        assert "save_support_message_controller" in dependencies
        assert "delete_template_controller" in dependencies
        assert "get_template_controller" in dependencies
        assert "get_template_list_controller" in dependencies
        assert "save_template_controller" in dependencies
        assert "registration_controller" in dependencies
        assert "authentication_controller" in dependencies
        assert "delete_conversation_controller" in dependencies
        assert "mark_done_support_message_controller" in dependencies
        assert "get_dashboard_metrics_controller" in dependencies