import pytest
from unittest.mock import MagicMock
from datetime import datetime
from repositories.message_postgres_repository import MessagePostgresRepository
from entities.message_entity import MessageEntity


@pytest.fixture
def message_repo():
    return MessagePostgresRepository({})


@pytest.fixture
def mock_cursor(mocker):
    mock_connection = mocker.patch('repositories.message_postgres_repository.psycopg2.connect')
    mock_conn_instance = mock_connection.return_value
    mock_cursor_instance = mock_conn_instance.cursor.return_value

    mock_conn_instance.__enter__.return_value = mock_conn_instance
    mock_cursor_instance.__enter__.return_value = mock_cursor_instance

    return mock_cursor_instance


def test_get_message(message_repo, mock_cursor):
    # Test case where message is found
    mock_cursor.fetchone.return_value = (30, "Hello World", datetime.now(), False, 1, True)

    message = message_repo.get_message(MessageEntity(id=30))

    assert message.id == 30
    assert message.text == "Hello World"

    # Test case where message is not found
    mock_cursor.fetchone.return_value = None

    with pytest.raises(ValueError, match="Message with ID 999 not found."):
        message_repo.get_message(MessageEntity(id=999))


def test_save_message(message_repo, mock_cursor):
    # Test case where save is successful
    mock_cursor.fetchone.return_value = [1]

    message = MessageEntity(
        id=None,
        text="Hello World",
        created_at=datetime.now(),
        conversation_id=1,
        rating=False
    )
    created_id = message_repo.save_message(message)

    assert created_id == 1
    mock_cursor.execute.assert_called_once()

    # Test case where save fails
    mock_cursor.execute.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        message_repo.save_message(message)


def test_get_messages_by_conversation(message_repo, mock_cursor):
    # Test case where messages are found
    mock_cursor.fetchall.return_value = [
        (1, "Hello World", datetime.now(), False, 1, True),
        (2, "Hi again", datetime.now(), False, 1, False)
    ]

    messages = message_repo.get_messages_by_conversation(MessageEntity(conversation_id=1))

    assert len(messages) == 2
    assert messages[0].id == 1
    assert messages[0].text == "Hello World"
    assert messages[1].id == 2
    assert messages[1].text == "Hi again"

    # Test case where no messages are found
    mock_cursor.fetchall.return_value = []

    messages = message_repo.get_messages_by_conversation(MessageEntity(conversation_id=999))

    assert len(messages) == 0


def test_fetch_messages(message_repo, mock_cursor):
    # Test case where messages are fetched
    mock_cursor.fetchall.return_value = [
        (1, "Hello World", datetime.now(), False, 1, True),
        (2, "Hi again", datetime.now(), False, 2, False)
    ]

    messages = message_repo.fetch_messages()

    assert len(messages) == 2
    assert messages[0].id == 1
    assert messages[0].text == "Hello World"
    assert messages[1].id == 2
    assert messages[1].text == "Hi again"

    # Test case where no messages are fetched
    mock_cursor.fetchall.return_value = []

    messages = message_repo.fetch_messages()

    assert len(messages) == 0

