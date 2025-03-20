import pytest
import psycopg2
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from config.db_config import db_config
from entities.conversation_entity import ConversationEntity


@pytest.fixture
def repository():
    """Fixture to create an instance of the repository."""
    return ConversationPostgresRepository(db_config)


def test_database_connection(repository):
    """Test if the database connection is successfully established."""
    try:
        conn = repository._ConversationPostgresRepository__connect()
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")


def test_get_conversation(repository):
    """Test retrieving a conversation from the database (ensure test data exists)."""
    conversation_entity = ConversationEntity(id=1, title="place holder")  # Replace with an existing conversation ID
    
    result_conversation = repository.get_conversation(conversation_entity)
    
    assert isinstance(result_conversation, ConversationEntity)
    assert result_conversation.get_id() == 1
    assert result_conversation.get_title() is not None


def test_get_conversation_none(repository):
    """Test retrieving a non-existing conversation from the database."""
    conversation_entity = ConversationEntity(id=-1, title="place holder")  # Non-existing ID in your database
    result_conversation = repository.get_conversation(conversation_entity)

    assert result_conversation is None, "Conversation not found in database"


def test_get_conversations(repository):
    """Test retrieving all conversations from the database."""
    result_conversations = repository.get_conversations()

    assert result_conversations is not None, "No conversations found in the database"
    assert isinstance(result_conversations, list)
    assert all(isinstance(conversation, ConversationEntity) for conversation in result_conversations)

    for conversation in result_conversations:
        assert conversation.get_id() is not None
        assert conversation.get_title() is not None


def test_save_conversation_title(repository):
    """Test saving a conversation title in the database."""
    try:
        title = "Test Conversation"
        conversation_entity = ConversationEntity(title=title)

        # Save the conversation
        result = repository.save_conversation_title(conversation_entity)
        assert result is True, "Failed to save conversation"

        # Verify the saved conversation by retrieving it
        saved_conversations = repository.get_conversations()
        saved_conversation = next(
            (conv for conv in saved_conversations if conv.get_title() == title), None
        )
        assert saved_conversation is not None, "Saved conversation not found in database"
        assert saved_conversation.get_title() == title, "Title mismatch"

    except Exception as e:
        pytest.fail(f"Saving conversation failed: {e}")
