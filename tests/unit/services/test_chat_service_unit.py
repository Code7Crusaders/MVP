import pytest
from unittest.mock import MagicMock
from services.chat_service import ChatService
from services.similarity_search_service import SimilaritySearchService
from services.generate_answer_service import GenerateAnswerService
from models.question_model import QuestionModel
from models.answer_model import AnswerModel

@pytest.fixture
def similarity_search_service_mock():
    return MagicMock(spec=SimilaritySearchService)

@pytest.fixture
def generate_answer_service_mock():
    return MagicMock(spec=GenerateAnswerService)

@pytest.fixture
def chat_service(similarity_search_service_mock, generate_answer_service_mock):
    return ChatService(similarity_search_service_mock, generate_answer_service_mock)

# Test get_answer

def test_get_answer_valid(chat_service, similarity_search_service_mock, generate_answer_service_mock):
    question = QuestionModel(question="What is AI?")
    context = ["AI stands for Artificial Intelligence."]
    answer = AnswerModel(answer="AI stands for Artificial Intelligence.")

    similarity_search_service_mock.similarity_search.return_value = context
    generate_answer_service_mock.generate_answer.return_value = answer

    result = chat_service.get_answer(question)
    
    assert result == answer
    similarity_search_service_mock.similarity_search.assert_called_once_with(question)
    generate_answer_service_mock.generate_answer.assert_called_once_with(question, context)

def test_get_answer_no_context(chat_service, similarity_search_service_mock, generate_answer_service_mock):
    question = QuestionModel(question="Unknown question")
    context = []
    answer = AnswerModel(answer="I don't know.")

    similarity_search_service_mock.similarity_search.return_value = context
    generate_answer_service_mock.generate_answer.return_value = answer

    result = chat_service.get_answer(question)
    
    assert result == answer
    similarity_search_service_mock.similarity_search.assert_called_once_with(question)
    generate_answer_service_mock.generate_answer.assert_called_once_with(question, context)

def test_get_answer_exception(chat_service, similarity_search_service_mock, generate_answer_service_mock):
    question = QuestionModel(question="What is AI?")
    similarity_search_service_mock.similarity_search.side_effect = Exception("Similarity search error")
    
    with pytest.raises(Exception) as exc_info:
        chat_service.get_answer(question)
    
    assert "Similarity search error" in str(exc_info.value)
    similarity_search_service_mock.similarity_search.assert_called_once_with(question)
