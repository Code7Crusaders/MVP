import pytest
from unittest.mock import MagicMock, ANY
from controllers.save_conversation_title_controller import SaveConversationTitleController
from usecases.save_conversation_title_useCase import SaveConversationTitleUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

@pytest.fixture
def save_conversation_title_use_case_mock():
    return MagicMock(spec=SaveConversationTitleUseCase)

@pytest.fixture
def save_conversation_title_controller(save_conversation_title_use_case_mock):
    return SaveConversationTitleController(save_conversation_title_use_case_mock)

# Test save_conversation_title

def test_save_conversation_title_valid(save_conversation_title_controller, save_conversation_title_use_case_mock):
    conversation_dto = ConversationDTO(id=1, title="Test Conversation Title")

    # Mock the save_conversation_title method
    save_conversation_title_use_case_mock.save_conversation_title.return_value = 1

    # Call the controller method
    result = save_conversation_title_controller.save_conversation_title(conversation_dto)

    # Assert the result is the expected conversation ID
    assert result == 1
    
    # Ensure that a ConversationModel instance with correct attributes was passed to the mock
    save_conversation_title_use_case_mock.save_conversation_title.assert_called_once()
    
    # Check if the call was made with the expected arguments
    called_arg = save_conversation_title_use_case_mock.save_conversation_title.call_args[0][0]
    assert isinstance(called_arg, ConversationModel)
    assert called_arg.id == conversation_dto.id
    assert called_arg.title == conversation_dto.title

def test_save_conversation_title_exception(save_conversation_title_controller, save_conversation_title_use_case_mock):
    conversation_dto = ConversationDTO(id=2, title="Error Conversation Title")
    
    # Simulate an exception during the save process
    save_conversation_title_use_case_mock.save_conversation_title.side_effect = Exception("Database error")
    
    # Check if the exception is properly raised
    with pytest.raises(Exception) as exc_info:
        save_conversation_title_controller.save_conversation_title(conversation_dto)
    
    # Assert the exception message
    assert str(exc_info.value) == "Database error"
    save_conversation_title_use_case_mock.save_conversation_title.assert_called_once()
