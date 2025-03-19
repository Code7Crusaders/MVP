import pytest
import psycopg2
from repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from config.db_config import db_config
from entities.support_message_entity import SupportMessageEntity


@pytest.fixture
def repository():
    """Fixture to create an instance of the repository."""
    return SupportMessagePostgresRepository(db_config)

def test_database_connection(repository):
    """Test if the database connection is successfully established."""
    try:
        conn = repository._SupportMessagePostgresRepository__connect()  # Access private method
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")

def test_get_support_message(repository):
    """Test retrieving a support message from the database (ensure test data exists)."""
    message_id = 1  # existing ID in your DB
    message = repository.get_support_message(message_id)
    assert message is not None, "Message not found in database"
    assert isinstance(message, SupportMessageEntity)


def test_get_support_message_none(repository):
    """Test retrieving a non-existing support message from the database."""
    message_id = -1  # non-existing ID in your DB
    message = repository.get_support_message(message_id)
    assert message is None, "Message found in database"


def test_get_support_messages(repository):
    """Test retrieving all support messages from the database."""
    messages = repository.get_support_messages()
    assert isinstance(messages, list), "Messages should be a list"
    if messages:  # If there are messages in the database
        assert all(isinstance(message, SupportMessageEntity) for message in messages), "All items should be SupportMessageEntity instances"


def test_save_delete_support_message(repository):
    """Test saving and deleting a support message in the database."""
    user_id = 1  # Replace with a valid user ID in your database
    description = "Test support message"
    status = "true"  # Assuming status is stored as a boolean in the database
    subject = "Test Subject"

    try:
        
        message_id = repository.save_support_message(user_id, description, status, subject)
        
        assert message_id is not None, "Failed to save support message"
        assert isinstance(message_id, int), "Message ID should be an integer"

        # Verify the saved message by retrieving it
        saved_message = repository.get_support_message(message_id)

        assert saved_message is not None, "Saved message not found in database"
        assert saved_message.user_id == user_id, "User ID mismatch"
        assert saved_message.description == description, "Description mismatch"
        assert saved_message.status == (status == "true"), "Status mismatch"
        assert saved_message.subject == subject, "Subject mismatch"
    except Exception as e:
        pytest.fail(f"Saving support message failed: {e}")

    try:
        # Delete the saved message
        repository.delete_support_message(message_id)
        deleted_message = repository.get_support_message(message_id)
        assert deleted_message is None, "Failed to delete support message"
    except Exception as e:
        pytest.fail(f"Deleting support message failed: {e}")

    

    
