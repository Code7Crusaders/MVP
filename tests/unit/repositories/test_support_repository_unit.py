import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from entities.support_message_entity import SupportMessageEntity
from config.db_config import db_config
@pytest.fixture
def support_message_repo():
    return SupportMessagePostgresRepository(db_config)


@pytest.fixture
def mock_cursor(mocker):
    mock_connection = mocker.patch('repositories.support_message_postgres_repository.psycopg2.connect')
    mock_conn_instance = mock_connection.return_value
    mock_cursor_instance = mock_conn_instance.cursor.return_value

    mock_conn_instance.__enter__.return_value = mock_conn_instance
    mock_cursor_instance.__enter__.return_value = mock_cursor_instance

    return mock_cursor_instance


def test_get_support_message(support_message_repo, mock_cursor):
    # Test case where support message is found
    mock_cursor.fetchone.return_value = (1, 1, "Test Description", "true", "Test Subject", "2023-01-01")
    support_message = SupportMessageEntity(
        id=1,
        user_id=1,
        description="Test Description",
        status="true",
        subject="Test Subject",
        created_at=datetime.now()
    )
    support_message = support_message_repo.get_support_message(support_message)

    assert support_message.id == 1
    assert support_message.user_id == 1
    assert support_message.description == "Test Description"
    assert support_message.status == "true"
    assert support_message.subject == "Test Subject"
    assert support_message.created_at == "2023-01-01"

    # Test case where support message is not found
    mock_cursor.fetchone.return_value = None

    support_message = SupportMessageEntity(
        id=999,
        user_id=1,
        description="Test Description",
        status="true",
        subject="Test Subject",
        created_at=datetime.now()
    )

    with pytest.raises(ValueError, match=f"No support messages found for support message ID {support_message.id}."):
        support_message_repo.get_support_message(support_message)


def test_save_support_message(support_message_repo, mock_cursor):
    # Test case where save is successful
    mock_cursor.fetchone.return_value = [1]

    support_message = SupportMessageEntity(
        id=None,
        user_id=1,
        description="New Support Message Content",
        status="true",
        subject="New Subject",
        created_at=datetime.now()
    )
    created_id = support_message_repo.save_support_message(support_message)

    assert created_id == 1
    mock_cursor.execute.assert_called_once()

    # Test case where save fails
    mock_cursor.execute.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        support_message_repo.save_support_message(support_message)
        
def test_mark_done_support_messages(support_message_repo):
    
    support_message_entity = SupportMessageEntity(
        id=1,
        user_id=1,
        description="Test Description",
        status="true",
        subject="Test Subject",
        created_at=datetime.now()
    )

    result = support_message_repo.mark_done_support_messages(support_message_entity)

    assert result == 1
