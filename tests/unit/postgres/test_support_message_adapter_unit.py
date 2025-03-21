import pytest
from unittest.mock import MagicMock, ANY
from adapters.support_message_postgres_adapter import SupportMessagePostgresAdapter
from models.support_message_model import SupportMessageModel
from entities.support_message_entity import SupportMessageEntity

@pytest.fixture
def repository_mock():
    return MagicMock()

@pytest.fixture
def adapter(repository_mock):
    return SupportMessagePostgresAdapter(repository_mock)

# Test get_support_message

def test_get_support_message_valid(adapter, repository_mock):
    repository_mock.get_support_message.return_value = SupportMessageEntity(
        id=1, user_id=2, description="Test description", status="open", subject="Test subject", created_at="2023-01-01"
    )
    model = SupportMessageModel(id=1)
    
    result = adapter.get_support_message(model)
    
    assert isinstance(result, SupportMessageModel)
    assert result.id == 1
    assert result.user_id == 2
    assert result.description == "Test description"
    assert result.status == "open"
    assert result.subject == "Test subject"
    assert result.created_at == "2023-01-01"

def test_get_support_message_invalid_id(adapter, repository_mock):
    repository_mock.get_support_message.return_value = None
    
    model = SupportMessageModel(id=-1)

    with pytest.raises(Exception, match="'NoneType' object has no attribute 'get_id'"):  
        result = adapter.get_support_message(model)
    

# Test get_support_messages

def test_get_support_messages(adapter, repository_mock):
    repository_mock.get_support_messages.return_value = [
        MagicMock(id=1, user_id=2, description="Desc 1", status="open", subject="Subj 1", created_at="2023-01-01"),
        MagicMock(id=2, user_id=3, description="Desc 2", status="closed", subject="Subj 2", created_at="2023-01-02"),
    ]
    
    result = adapter.get_support_messages()
    
    assert len(result) == 2
    assert all(isinstance(msg, SupportMessageModel) for msg in result)
    assert result[0].id == 1
    assert result[1].id == 2

def test_get_support_messages_empty(adapter, repository_mock):
    repository_mock.get_support_messages.return_value = []
    
    result = adapter.get_support_messages()
    
    assert result == []

# Test save_support_message

def test_save_support_message_valid(adapter, repository_mock):

    support_message_model = SupportMessageModel(id=2, user_id=2, description="Test description", status="open", subject="Test subject", created_at="2023-01-01")
    support_message_entity = SupportMessageEntity(id=2, user_id=2, description="Test description", status="open", subject="Test subject", created_at="2023-01-01")

    adapter.save_support_message(support_message_model)
    
    repository_mock.save_support_message.assert_called_once_with(ANY)


def test_save_support_message_invalid_data(adapter, repository_mock):
    with pytest.raises(TypeError):
        adapter.save_support_message(None, None, None, None)
