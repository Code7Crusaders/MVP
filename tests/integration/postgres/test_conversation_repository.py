import pytest
import psycopg2
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from config.db_config import db_config
from entities.conversation_entity import ConversationEntity
from unittest.mock import patch, MagicMock

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


def test_get_conversation_error(repository, get_conversation_port_mock):
    """Test retrieving a non-existing conversation from the database."""
    conversation_entity = ConversationEntity(id=-1)
    get_conversation_port_mock.get_conversations.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        repository.get_conversation(conversation_entity)

    assert str(exc_info.value) == "Database error"
    get_conversation_port_mock.get_conversations.assert_called_once()



def test_get_conversations(conversation_postgres_repository: ConversationPostgresRepository, conversation_postgres_repository_mock: MagicMock):
    """Test retrieving all conversations from the database."""
    # Prepare the test data
    user_id = 1  # Replace with an existing user ID
    conversation_entity = ConversationEntity(id=None, title=None, user_id=user_id)
    
    # Mock the repository response
    mock_conversations = [
        ConversationEntity(id=1, title="Conversation 1", user_id=user_id),
        ConversationEntity(id=2, title="Conversation 2", user_id=user_id),
    ]
    
    # Mock the repository method
    conversation_postgres_repository_mock.get_conversations.return_value = mock_conversations

    # Call the method
    result_conversations = conversation_postgres_repository.get_conversations(conversation_entity)
    
    # Asserts
    assert result_conversations is not None, "No conversations found in the database"
    assert isinstance(result_conversations, list)
    assert all(isinstance(conversation, ConversationEntity) for conversation in result_conversations)

    for conversation in result_conversations:
        assert conversation.get_id() is not None
        assert conversation.get_title() is not None
        assert conversation.get_user_id() == user_id


def test_save_delete_conversation_title(repository): 
    """Test saving a conversation title in the database."""
    try:
        title = "Test Conversation" 
        conversation_entity = ConversationEntity(title=title)

        # Save the conversation
        result = repository.save_conversation_title(conversation_entity)
        assert isinstance(result, int), "Saved conversation ID is not an integer"

        # Verify the saved conversation by retrieving it
        saved_conversation = repository.get_conversation(ConversationEntity(id=result))

        assert saved_conversation is not None, "Saved conversation not found in database"
        assert saved_conversation.get_title() == title, "Title mismatch"

    except Exception as e:
        pytest.fail(f"Saving conversation failed: {e}")

    try:
        # Delete the saved conversation
        result = repository.delete_conversation(saved_conversation)
        assert result is True, "Conversation deletion failed"

        # Verify the deletion by ensuring retrieving it raises an error
        with pytest.raises(ValueError):
            repository.get_conversation(saved_conversation)
    
    except Exception as e:
        pytest.fail(f"Deleting conversation failed: {e}")
