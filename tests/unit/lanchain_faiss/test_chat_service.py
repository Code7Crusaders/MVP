import pytest
from unittest.mock import MagicMock
from app.services.chat_service import ChatService
from app.services.similarity_search_service import SimilaritySearchService
from app.services.generate_answer_service import GenerateAnswerService
from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel
from app.models.context_model import ContextModel


def test_get_answer_success():
    """
    Test successful chat response generation.
    """
    similarity_search_service_mock = MagicMock(spec=SimilaritySearchService)
    generate_answer_service_mock = MagicMock(spec=GenerateAnswerService)
    service = ChatService(similarity_search_service_mock, generate_answer_service_mock)

    question = QuestionModel("What is LangChain?")
    contexts = [ContextModel("LangChain is a framework for developing applications with LLMs.")]
    expected_answer = AnswerModel("LangChain is a framework that helps developers build applications with LLMs.")

    # Mocking 
    similarity_search_service_mock.similarity_search.return_value = contexts
    generate_answer_service_mock.generate_answer.return_value = expected_answer

    # Run 
    result = service.get_answer(question)

    # Assertions
    similarity_search_service_mock.similarity_search.assert_called_once_with(question)
    generate_answer_service_mock.generate_answer.assert_called_once_with(question, contexts)
    assert result == expected_answer


def test_get_answer_similarity_search_exception():
    """
    Test exception handling when similarity_search fails.
    """
    similarity_search_service_mock = MagicMock(spec=SimilaritySearchService)
    generate_answer_service_mock = MagicMock(spec=GenerateAnswerService)
    service = ChatService(similarity_search_service_mock, generate_answer_service_mock)

    question = QuestionModel("What is LangChain?")

    # Simulating an error in similarity search
    similarity_search_service_mock.similarity_search.side_effect = Exception("Similarity search failed")

    with pytest.raises(Exception, match="Similarity search failed"):
        service.get_answer(question)

    # Ensure generate_answer was never called
    generate_answer_service_mock.generate_answer.assert_not_called()


def test_get_answer_generate_answer_exception():
    """
    Test exception handling when generate_answer fails.
    """
    similarity_search_service_mock = MagicMock(spec=SimilaritySearchService)
    generate_answer_service_mock = MagicMock(spec=GenerateAnswerService)
    service = ChatService(similarity_search_service_mock, generate_answer_service_mock)

    question = QuestionModel("What is LangChain?")
    contexts = [ContextModel("LangChain is a framework for developing applications with LLMs.")]

    # Mock similarity search success
    similarity_search_service_mock.similarity_search.return_value = contexts
    generate_answer_service_mock.generate_answer.side_effect = Exception("Answer generation failed")

    with pytest.raises(Exception, match="Answer generation failed"):
        service.get_answer(question)

    # Ensure similarity_search was called, but generate_answer raised an error
    similarity_search_service_mock.similarity_search.assert_called_once_with(question)
    generate_answer_service_mock.generate_answer.assert_called_once_with(question, contexts)
