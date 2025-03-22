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
    assert result.created_at == "2023-01-01"

    repository_mock.get_support_message.assert_called_once()

def test_get_support_message_invalid_id(adapter, repository_mock):
    repository_mock.get_support_message.return_value = None
    message_model = SupportMessageModel(id=-1, user_id=2, description="Test description",
                                        status="open", subject="Test subject", created_at="2023-01-01")

    result = adapter.get_support_message(message_model)

    assert result is None  
    repository_mock.get_support_message.assert_called_once()
# Test get_support_messages

def test_get_support_messages(adapter, repository_mock):
    repository_mock.get_support_messages.return_value = [
        MagicMock(id=1, user_id=2, description="Desc 1", status="open", subject="Subj 1", created_at="2023-01-01"),
        MagicMock(id=2, user_id=3, description="Desc 2", status="closed", subject="Subj 2", created_at="2023-01-02"),
    ]
    
    result = adapter.get_support_messages()
    
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(msg, SupportMessageModel) for msg in result)
    assert result[0].id == 1
    assert result[0].subject == "Subj 1"
    assert result[1].id == 2
    assert result[1].status == "closed"

    repository_mock.get_support_messages.assert_called_once()

def test_get_support_messages_empty(adapter, repository_mock):
    repository_mock.get_support_messages.return_value = []
    
    result = adapter.get_support_messages()
    
    assert isinstance(result, list)
    assert result == []

    repository_mock.get_support_messages.assert_called_once()

# Test save_support_message

def test_save_support_message_valid(adapter, repository_mock):
    support_message = SupportMessageModel(
        id=None, user_id=2, description="Test description", status="open", subject="Test subject", created_at="2023-01-01"
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

    # Expecting the exception to be raised by the adapter
    with pytest.raises(Exception, match="Database error"):
        adapter.get_support_message(message_model)


def test_get_support_messages_exception(adapter, repository_mock):
    repository_mock.get_support_messages.side_effect = Exception("Database failure")
    
    # Expecting the exception to be raised by the adapter
    with pytest.raises(Exception, match="Database failure"):
        adapter.get_support_messages()


def test_save_support_message_exception(adapter, repository_mock):
    repository_mock.save_support_message.side_effect = Exception("Insert failed")

    support_message = SupportMessageModel(id=None, user_id=2, description="Test",
                                          status="open", subject="Test subject", created_at="2023-01-01")

    # Expecting the exception to be raised by the adapter
    with pytest.raises(Exception, match="Insert failed"):
        adapter.save_support_message(support_message)
