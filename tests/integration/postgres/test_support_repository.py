import pytest
import psycopg2
from datetime import datetime
import pytz

from repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from config.db_config import db_config
from entities.support_message_entity import SupportMessageEntity

italy_tz = pytz.timezone('Europe/Rome')


@pytest.fixture
def repository():
    """Fixture to create an instance of the repository."""
    return SupportMessagePostgresRepository(db_config)

def test_database_connection(repository):
    """Test if the database connection is successfully established."""
    try:
        conn = repository._SupportMessagePostgresRepository__connect() 
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")

def test_get_support_message(repository):
    """Test retrieving a support message from the database (ensure test data exists)."""
    support_message_entity = SupportMessageEntity( id=1) #get only needs the id
    
    result_message = repository.get_support_message(support_message_entity)
    
    assert isinstance(result_message, SupportMessageEntity)
    assert result_message.get_id() == 1
    assert result_message.get_user_id() is not None
    assert result_message.get_description() is not None
    assert result_message.get_status() is not None
    assert result_message.get_subject() is not None
    assert result_message.get_created_at() is not None

def test_get_support_message_none(repository):
    """Test retrieving a non-existing support message from the database."""
    support_message_entity = SupportMessageEntity(id=-1)  # non-existing ID in your DB

    result_message = repository.get_support_message(support_message_entity)

    assert result_message is None, "Message found in database"


def test_get_support_messages(repository):
    """Test retrieving all support messages from the database."""
    messages = repository.get_support_messages()
    assert isinstance(messages, list), "Messages should be a list"
    if messages:  # If there are messages in the database
        assert all(isinstance(message, SupportMessageEntity) for message in messages), "All items should be SupportMessageEntity instances"


def test_save_delete_support_message(repository):
    """Test saving and deleting a support message in the database."""
    try:
        user_id = 1  # Replace with a valid user ID in your database
        description = "Test support message"
        status = True  # Assuming status is stored as a boolean in the database
        subject = "Test Subject"
        created_at = datetime.now(italy_tz)
        

        support_message_entity = SupportMessageEntity(user_id=user_id, description=description, status=status, subject=subject, created_at=created_at)

        saved_id = repository.save_support_message(support_message_entity)
        
        assert saved_id is not None, "Failed to save support message"
        

        # Verify the saved message by retrieving it
        saved_message = repository.get_support_message(SupportMessageEntity(id=saved_id))

        assert saved_message is not None, "Saved message not found in database"
        assert saved_message.get_user_id() == user_id, "User ID mismatch"
        assert saved_message.get_description() == description, "Description mismatch"
        assert saved_message.get_status() == status, "Status mismatch"
        assert saved_message.get_subject() == subject, "Subject mismatch"
        assert saved_message.get_created_at() == created_at, "Created at mismatch"
        assert saved_message.get_id() == saved_id, "ID mismatch"

    except Exception as e:
        pytest.fail(f"Saving support message failed: {e}")

    try:
        delete_message = SupportMessageEntity(id=saved_id)
        result = repository.delete_support_message(delete_message)

        assert result is True, "Failed to delete support message"

    except Exception as e:
        pytest.fail(f"Deleting support message failed: {e}") 

    
def test_save_support_message_fail(repository):
    """Test saving a support message with invalid data to ensure it fails."""
    try:
        # Create a support message entity with invalid data (e.g., missing required fields)
        invalid_support_message_entity = SupportMessageEntity(user_id=None, description=None, status=None, subject=None, created_at=None)
        # Attempt to save the invalid support message
        result = repository.save_support_message(invalid_support_message_entity)
        
        assert result is None

        pytest.fail("Saving invalid support message should have failed, but it succeeded.")
    except Exception:
        # Expected behavior: an exception should be raised
        pass
    
