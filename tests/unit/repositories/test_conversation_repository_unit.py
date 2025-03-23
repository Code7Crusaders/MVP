import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from config.db_config import db_config

from entities.conversation_entity import ConversationEntity


@pytest.fixture
def conversation_repo():
    return ConversationPostgresRepository(db_config)


def test_get_conversation(conversation_repo):

    conversation = ConversationEntity(id=4, title="Test Conversation")

    conversation_ciao = conversation_repo.get_conversation(conversation)
    
    assert conversation_ciao is not None
    assert conversation_ciao.get_id() == 4
    assert conversation_ciao.get_title() == "Casual Conversations"

    # # Test case where conversation is not found
    # mock_get_conversation.return_value = None

    conversation = ConversationEntity(id=-1, title="Test Conversation")

    with pytest.raises(ValueError):
        conversation_repo.get_conversation(conversation)
    

def test_save_conversation_title(conversation_repo):

    conversation = ConversationEntity(title="Hi there")

    result = conversation_repo.save_conversation_title(conversation)
    
    assert result is not None

