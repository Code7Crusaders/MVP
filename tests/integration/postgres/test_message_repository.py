import pytest
import psycopg2
from datetime import datetime
import pytz

from repositories.message_postgres_repository import MessagePostgresRepository
from config.db_config import db_config
from entities.message_entity import MessageEntity
from entities.conversation_entity import ConversationEntity


italy_tz = pytz.timezone('Europe/Rome')


@pytest.fixture
def repository():
    """Fixture to create an instance of the repository."""
    return MessagePostgresRepository(db_config)


def test_database_connection(repository):
    """Test if the database connection is successfully established."""
    try:
        conn = repository._MessagePostgresRepository__connect()
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")


def test_get_message(repository):
    """Test retrieving a message from the database (ensure test data exists)."""
    message_entity = MessageEntity(id=1)  # get only needs the id
    
    result_message = repository.get_message(message_entity)
    
    assert isinstance(result_message, MessageEntity)
    assert result_message.get_id() == 1
    assert result_message.get_text() is not None
    assert result_message.get_rating() is None or isinstance(result_message.get_rating(), bool)
    assert result_message.get_conversation_id() is not None
    assert result_message.get_created_at() is not None


def test_get_message_error(repository):
    """Test retrieving a non-existing message from the database."""
    message_entity = MessageEntity(id=-1)  # Non-existing ID in your database
    with pytest.raises(ValueError):
        repository.get_message(message_entity)

def test_get_messages_by_conversation(repository):
    """Test retrieving messages by conversation from the database."""
    conversation = MessageEntity(conversation_id=1)  # get only needs the conversation_id
    result_messages = repository.get_messages_by_conversation(conversation)

    assert result_messages is not None, "Messages not found for the given conversation"
    assert isinstance(result_messages, list)
    assert all(isinstance(message, MessageEntity) for message in result_messages)

    for message in result_messages:
        assert message.get_conversation_id() == conversation.get_conversation_id()
        assert message.get_text() is not None
        assert message.get_created_at() is not None
        assert message.get_rating() is None or isinstance(message.get_rating(), bool)


def test_get_messages_by_conversation_empty(repository):
    """Test retrieving messages for a conversation with no messages."""
    conversation = MessageEntity(conversation_id=-1)  # Non-existing conversation ID in your database
    with pytest.raises(ValueError):
        repository.get_messages_by_conversation(conversation)

def test_save_delete_message(repository):
    """Test saving and deleting a message in the database."""
    try:
        text = "Test message"
        created_at = datetime.now(italy_tz)
        user_id = 1  # Replace with a valid user ID in your database
        conversation_id = 1  # Replace with a valid conversation ID in your database
        rating = True  # Assuming rating is stored as a boolean in the database

        message_entity = MessageEntity(
            text=text,
            created_at=created_at,
            user_id=user_id,
            conversation_id=conversation_id,
            rating=rating
        )

        # Save the message
        saved_id = repository.save_message(message_entity)
        assert saved_id is not None, "Failed to save message"
        message_entity = MessageEntity(id=saved_id)  # get only needs the id

        # Verify the saved message by retrieving it
        saved_message = repository.get_message(message_entity)  # Pass the instance with the correct id
        assert saved_message is not None, "Saved message not found in database"
        assert saved_message.get_text() == text, "Text mismatch"
        assert saved_message.get_created_at() == created_at, "Created at mismatch"
        assert saved_message.get_rating() == rating, "Rating mismatch"
        assert saved_message.get_id() == saved_id, "ID mismatch"  # Ensure get_id() is called correctly

    except Exception as e:
        pytest.fail(f"Saving message failed: {e}")

    try:
        # Delete the message
        delete_message = MessageEntity(id=saved_id)
        result = repository.delete_message(delete_message)
        assert result is True, "Failed to delete message"

        # Verify the message is deleted
        with pytest.raises(ValueError):
            deleted_message = repository.get_message(delete_message)  # Pass the instance with the correct id

    except Exception as e:
        pytest.fail(f"Deleting message failed: {e}")


def test_save_message_fail(repository):
    """Test saving a message with invalid data to ensure it fails."""
    try:
        invalid_message_entity = MessageEntity(
            text=None,  # Missing text
            created_at=None,  # Missing created_at
            user_id=None,  # Missing user_id
            conversation_id=None,  # Missing conversation_id
            rating=None  # Missing rating
        )
        result = repository.save_message(invalid_message_entity)
        
        assert result is None

        pytest.fail("Saving invalid message should have failed, but it succeeded.")
    except Exception:
        # Expected behavior: an exception should be raised
        pass