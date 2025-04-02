import pytest
from unittest.mock import MagicMock, ANY
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from models.conversation_model import ConversationModel
from adapters.conversation_postgres_adapter import ConversationPostgresAdapter
from entities.conversation_entity import ConversationEntity

@pytest.fixture 
def conversation_postgres_repository_mock():
    return MagicMock(spec=ConversationPostgresRepository)

@pytest.fixture
def conversation_postgres_adapter(conversation_postgres_repository_mock: MagicMock):
    return ConversationPostgresAdapter(conversation_postgres_repository_mock)

# Test get_conversation

def test_get_conversation_valid(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Test Conversation", user_id=1)
    
    # Mock repository response
    conversation_postgres_repository_mock.get_conversation.return_value = conversation_model

    result = conversation_postgres_adapter.get_conversation(conversation_model)
    
    assert result.get_id() == 1
    assert result.get_title() == "Test Conversation"
    assert result.get_user_id() == 1

def test_get_conversation_not_found(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Test Conversation", user_id=1)
    
    # Simulate repository exception
    conversation_postgres_repository_mock.get_conversation.side_effect = Exception("Conversation not found")
    
    with pytest.raises(Exception, match="Conversation not found"):
        conversation_postgres_adapter.get_conversation(conversation_model)

# Test get_conversations

def test_get_conversations_valid(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversations = [
        ConversationModel(id=1, title="Conversation 1", user_id=1),
        ConversationModel(id=2, title="Conversation 2", user_id=1),
    ]
    
    user_id = 1

    # Mock repository response
    conversation_postgres_repository_mock.get_conversations.return_value = conversations

    result = conversation_postgres_adapter.get_conversations(ConversationModel(id=None, title=None, user_id=user_id))
    
    assert len(result) == 2
    assert result[0].get_title() == "Conversation 1"
    assert result[1].get_title() == "Conversation 2"

def test_get_conversations_empty(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    # Mock repository response with no conversations
    conversation_postgres_repository_mock.get_conversations.return_value = []

    user_id = 1

    result = conversation_postgres_adapter.get_conversations(ConversationModel(id=None, title=None, user_id=user_id))
    
    assert result == []

# Test save_conversation_title

def test_save_conversation_title_valid(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Updated Title", user_id=1)
    
    # Mock repository response
    conversation_postgres_repository_mock.save_conversation_title.return_value = 1  # Assume returning the conversation ID

    result = conversation_postgres_adapter.save_conversation_title(conversation_model)
    
    conversation_postgres_repository_mock.save_conversation_title.assert_called_once_with(ANY)
    assert isinstance(result, int)  # Ensure it returns an integer (conversation ID)

def test_save_conversation_title_failure(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Updated Title", user_id=1)
    
    # Simulate repository exception
    conversation_postgres_repository_mock.save_conversation_title.side_effect = Exception("Failed to save title")
    
    with pytest.raises(Exception, match="Failed to save title"):
        conversation_postgres_adapter.save_conversation_title(conversation_model)


def test_get_conversations_exception(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_postgres_repository_mock.get_conversations.side_effect = Exception("Database error")

    user_id = 1

    with pytest.raises(Exception, match="Database error"):
        conversation_postgres_adapter.get_conversations(ConversationModel(id=None, title=None, user_id=user_id))


def test_delete_conversation_title_valid(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Title to Delete", user_id=1)
        
    conversation_postgres_repository_mock.delete_conversation.return_value = True  
    result = conversation_postgres_adapter.delete_conversation_title(conversation_model)
        
    conversation_postgres_repository_mock.delete_conversation.assert_called_once_with(ANY)
    assert result is True  


def test_delete_conversation_title_failure(conversation_postgres_adapter: ConversationPostgresAdapter, conversation_postgres_repository_mock: MagicMock):
    conversation_model = ConversationModel(id=1, title="Title to Delete", user_id=1)
            
    conversation_postgres_repository_mock.delete_conversation.side_effect = Exception("Failed to delete conversation")
            
    with pytest.raises(Exception, match="Failed to delete conversation"):
        conversation_postgres_adapter.delete_conversation_title(conversation_model)
