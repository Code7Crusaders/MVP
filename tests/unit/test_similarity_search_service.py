import pytest
from unittest.mock import Mock
from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel
from app.ports.similarity_search_port import SimilaritySearchPort
from app.services.similarity_search_service import SimilaritySearchService

def test_similarity_search_success():
    # Arrange
    mock_port = Mock(spec=SimilaritySearchPort)
    service = SimilaritySearchService(mock_port)
    question = QuestionModel(user_id=1, question="What is AI?")
    expected_contexts = [ContextModel(content="Artificial Intelligence is...")]
    mock_port.similarity_search.return_value = expected_contexts

    # Act
    result = service.similarity_search(question)

    # Assert
    assert result == expected_contexts
    mock_port.similarity_search.assert_called_once_with(question)

def test_similarity_search_failure():
    # Arrange
    mock_port = Mock(spec=SimilaritySearchPort)
    service = SimilaritySearchService(mock_port)
    question = QuestionModel(user_id=1, question="What is AI?")
    mock_port.similarity_search.side_effect = Exception("Search failed")

    # Act & Assert
    with pytest.raises(Exception, match="Search failed"):
        service.similarity_search(question)
    mock_port.similarity_search.assert_called_once_with(question)