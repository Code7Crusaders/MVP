import pytest
from unittest.mock import MagicMock, ANY
from app.controllers.chat_controller import ChatController
from app.usecases.chat_useCase import ChatUseCase
from app.dto.QuestionDTO import QuestionDTO
from app.dto.AnswerDTO import AnswerDTO
from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel

@pytest.fixture
def mock_chat_usecase():
    """
    Mock per ChatUseCase.
    """
    mock = MagicMock(spec=ChatUseCase)
    mock.get_answer.return_value = AnswerModel("Test answer")  
    return mock

@pytest.fixture
def chat_controller(mock_chat_usecase):
    """
    Istanza di ChatController con il mock di ChatUseCase.
    """
    return ChatController(chat_usecase=mock_chat_usecase)

def test_get_answer_success():
    """
    Test to verify the correct functionality of get_answer.
    """
    # Arrange
    mock_chat_usecase = MagicMock(spec=ChatUseCase)
    mock_chat_usecase.get_answer.return_value = AnswerModel("Test answer")
    chat_controller = ChatController(mock_chat_usecase)
    
    question_dto = QuestionDTO(1, "What is AI?")
    
    # Act
    answer_dto = chat_controller.get_answer(question_dto)
    
    # Assert
    assert isinstance(answer_dto, AnswerDTO)
    assert answer_dto.get_answer() == "Test answer"
    
    # Ensure the mocked method was called with any QuestionModel instance
    mock_chat_usecase.get_answer.assert_called_with(ANY)

def test_get_answer_exception(chat_controller, mock_chat_usecase):
    """
    Test per verificare che un'eccezione venga gestita correttamente.
    """
    # Arrange
    mock_chat_usecase.get_answer.side_effect = Exception("Mocked error")
    question_dto = QuestionDTO(1, "What is AI?")
    
    # Act & Assert
    with pytest.raises(Exception, match="Mocked error"):
        chat_controller.get_answer(question_dto)
