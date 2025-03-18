import pytest
from unittest.mock import MagicMock, patch
from adapters.faiss_adapter import FaissAdapter
from repositories.faiss_repository import FaissRepository
from models.question_model import QuestionModel
from models.context_model import ContextModel
from models.file_chunk_model import FileChunkModel
from entities.query_entity import QueryEntity
from entities.file_chunk_entity import FileChunkEntity

@pytest.fixture
def faiss_repository_mock():
    return MagicMock(spec=FaissRepository)

@pytest.fixture
def faiss_adapter(faiss_repository_mock):
    return FaissAdapter(faiss_repository_mock)

# Test similarity_search

def test_similarity_search_valid_question(faiss_adapter, faiss_repository_mock):
    question_model = QuestionModel(user_id=1, question="What is AI?")
    
    # Mock repository response
    faiss_repository_mock.similarity_search.return_value = [
        ContextModel(content="AI stands for Artificial Intelligence."),
        ContextModel(content="AI is the simulation of human intelligence.")
    ]

    
    result = faiss_adapter.similarity_search(question_model)
    
    assert len(result) == 2
    assert all(isinstance(item, ContextModel) for item in result)
    assert result[0].get_content() == "AI stands for Artificial Intelligence."
    assert result[1].get_content() == "AI is the simulation of human intelligence."


def test_similarity_search_empty_question(faiss_adapter):
    question_model = QuestionModel(user_id=1, question="  ")  # Empty question
    with pytest.raises(ValueError, match="Question cannot be empty"):
        faiss_adapter.similarity_search(question_model)


# Test load_chunks

def test_load_chunks_valid(faiss_adapter, faiss_repository_mock):
    chunks = [
        FileChunkModel("Chunk 1 content", "Metadata 1"),
        FileChunkModel("Chunk 2 content", "Metadata 2"),
    ]

    faiss_repository_mock.load_chunks.return_value = "Success"

    faiss_adapter.load_chunks(chunks)

    # Check if the mocked function was actually called
    faiss_repository_mock.load_chunks.assert_called_once()



def test_load_chunks_empty(faiss_adapter):
    with pytest.raises(ValueError, match="No chunks to load."):
        faiss_adapter.load_chunks([])


def test_load_chunks_repository_exception(faiss_adapter, faiss_repository_mock):
    chunks = [FileChunkModel("Chunk 1 content", "Metadata 1")]
    faiss_repository_mock.load_chunks.side_effect = Exception("Failed to load chunks")
    
    result = faiss_adapter.load_chunks(chunks)
    
    assert result == "Failed to load chunks"

def test_similarity_search_repository_exception(faiss_adapter, faiss_repository_mock):
    question_model = QuestionModel(user_id=1, question="What is AI?")
    
    # Simulate an exception in the repository
    faiss_repository_mock.similarity_search.side_effect = Exception("Repository error")
    
    result = faiss_adapter.similarity_search(question_model)
    
    assert result == "Repository error"


def test_similarity_search_invalid_question_model(faiss_adapter):
    
    invalid_question_model = MagicMock()
    invalid_question_model.get_question.side_effect = AttributeError("Invalid question model")

    with pytest.raises(AttributeError, match="Invalid question model"):
        faiss_adapter.similarity_search(invalid_question_model)
