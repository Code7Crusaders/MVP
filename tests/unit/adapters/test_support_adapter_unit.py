import pytest
from unittest.mock import MagicMock
from adapters.support_message_postgres_adapter import SupportMessagePostgresAdapter
from models.support_message_model import SupportMessageModel

@pytest.fixture
def repository_mock():
    return MagicMock()

@pytest.fixture
def adapter(repository_mock):
    return SupportMessagePostgresAdapter(repository_mock)

# Test get_support_message

def test_get_support_message_valid(adapter, repository_mock):
    support_message_mock = MagicMock()
    support_message_mock.get_id.return_value = 1
    support_message_mock.get_user_id.return_value = 2
    support_message_mock.get_description.return_value = "Test description"
    support_message_mock.get_status.return_value = "open"
    support_message_mock.get_subject.return_value = "Test subject"
    support_message_mock.get_created_at.return_value = "2023-01-01"

    repository_mock.get_support_message.return_value = support_message_mock

    message_model = SupportMessageModel(id=1, user_id=2, description="Test description",
                                        status="open", subject="Test subject", created_at="2023-01-01")

    result = adapter.get_support_message(message_model)

    assert isinstance(result, SupportMessageModel)
    assert result.id == 1
    assert result.user_id == 2
    assert result.description == "Test description"
    assert result.status == "open"
    assert result.subject == "Test subject"

def test_mark_done_support_messages_valid(adapter, repository_mock):
    support_message = SupportMessageModel(
        id=1, user_id=2, description="Test description", status="done", subject="Test subject", created_at="2023-01-01"
    )

    repository_mock.mark_done_support_messages.return_value = 1

    result = adapter.mark_done_support_messages(support_message)

    assert isinstance(result, int)
    assert result == 1
    repository_mock.mark_done_support_messages.assert_called_once()

def test_mark_done_support_messages_invalid_id(adapter, repository_mock):
    support_message = SupportMessageModel(
        id=None, user_id=2, description="Test description", status="done", subject="Test subject", created_at="2023-01-01"
    )

    repository_mock.mark_done_support_messages.return_value = None

    result = adapter.mark_done_support_messages(support_message)

    assert result is None
    repository_mock.mark_done_support_messages.assert_called_once()

def test_mark_done_support_messages_exception(adapter, repository_mock):
    repository_mock.mark_done_support_messages.side_effect = Exception("Update failed")

    support_message = SupportMessageModel(
        id=1, user_id=2, description="Test description", status="done", subject="Test subject", created_at="2023-01-01"
    )

    with pytest.raises(Exception, match="Update failed"):
        adapter.mark_done_support_messages(support_message)

def test_save_support_message_valid(adapter, repository_mock):
    support_message = SupportMessageModel(
        id=1, user_id=2, description="Test description", status="open", subject="Test subject", created_at="2023-01-01"
    )

    repository_mock.save_support_message.return_value = 1

    result = adapter.save_support_message(support_message)

    assert isinstance(result, int)
    assert result == 1
    repository_mock.save_support_message.assert_called_once()

def test_save_support_message_invalid_data(adapter, repository_mock):
    invalid_message = SupportMessageModel(id=None, user_id=None, description="", status=None, subject=None, created_at=None)
    
    repository_mock.save_support_message.return_value = None  

    result = adapter.save_support_message(invalid_message)

    assert result is None
    repository_mock.save_support_message.assert_called_once()

def test_get_support_message_exception(adapter, repository_mock):
    repository_mock.get_support_message.side_effect = Exception("Database error")
    
    message_model = SupportMessageModel(id=1, user_id=2, description="Test",
                                        status="open", subject="Test subject", created_at="2023-01-01")

    with pytest.raises(Exception, match="Database error"):
        adapter.get_support_message(message_model)

def test_get_support_messages_exception(adapter, repository_mock):
    repository_mock.get_support_messages.side_effect = Exception("Database failure")
    
    with pytest.raises(Exception, match="Database failure"):
        adapter.get_support_messages()

def test_save_support_message_exception(adapter, repository_mock):
    repository_mock.save_support_message.side_effect = Exception("Insert failed")

    support_message = SupportMessageModel(id=None, user_id=2, description="Test",
                                          status="open", subject="Test subject", created_at="2023-01-01")

    with pytest.raises(Exception, match="Insert failed"):
        adapter.save_support_message(support_message)

def test_get_support_messages_valid(adapter, repository_mock):
    # Mock support message entities returned by the repository
    support_message_entity_1 = MagicMock(
        id=1,
        user_id=2,
        user_email="user1@example.com",
        description="Test description 1",
        status="open",
        subject="Test subject 1",
        created_at="2023-01-01"
    )
    support_message_entity_2 = MagicMock(
        id=2,
        user_id=3,
        user_email="user2@example.com",
        description="Test description 2",
        status="done",
        subject="Test subject 2",
        created_at="2023-01-02"
    )

    repository_mock.get_support_messages.return_value = [support_message_entity_1, support_message_entity_2]

    # Call the adapter method
    result = adapter.get_support_messages()

    # Assertions
    assert isinstance(result, list)
    assert len(result) == 2

    # Verify the first message
    assert result[0].id == 1
    assert result[0].user_id == 2
    assert result[0].user_email == "user1@example.com"
    assert result[0].description == "Test description 1"
    assert result[0].status == "open"
    assert result[0].subject == "Test subject 1"
    assert result[0].created_at == "2023-01-01"

    # Verify the second message
    assert result[1].id == 2
    assert result[1].user_id == 3
    assert result[1].user_email == "user2@example.com"
    assert result[1].description == "Test description 2"
    assert result[1].status == "done"
    assert result[1].subject == "Test subject 2"
    assert result[1].created_at == "2023-01-02"

    # Verify the repository method was called once
    repository_mock.get_support_messages.assert_called_once()
