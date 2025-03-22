import pytest
import os
from dotenv import load_dotenv
from unittest.mock import MagicMock, patch

from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from repositories.faiss_repository import FaissRepository
from entities.document_context_entity import DocumentContextEntity
from entities.query_entity import QueryEntity
from entities.file_chunk_entity import FileChunkEntity

@pytest.fixture
def mock_vector_store():
    mock_vector_store = MagicMock(spec=FAISS)
    return mock_vector_store

@pytest.fixture 
def mock_faiss_repo(mock_vector_store):
    return FaissRepository(mock_vector_store)


def test_similarity_search(mock_faiss_repo, mock_vector_store):
        
    mock_vector_store.similarity_search = MagicMock(return_value=[
        Document("Hello world 1"),
        Document("Hello world 2"),
        Document("Hello world 3"),
        Document("Hello world 4")
    ])
        
    query = QueryEntity(1, "Hello")
    
    result = mock_faiss_repo.similarity_search(query)
    
    assert len(result) == 4
    assert all(isinstance(doc, DocumentContextEntity) for doc in result)
    assert result[0].content == "Hello world 1"
    assert result[1].content == "Hello world 2"
    assert result[2].content == "Hello world 3"
    assert result[3].content == "Hello world 4"


def test_similarity_search_empty_query(mock_faiss_repo):
    query = QueryEntity(1, "")
    
    with pytest.raises(ValueError, match="Query cannot be empty"):
        mock_faiss_repo.similarity_search(query)


def test_similarity_search_exeption(mock_faiss_repo):
    mock_faiss_repo.vectorstore.similarity_search.side_effect = Exception("Mocked error")
    
    query = QueryEntity(1, "Hello")
    
    result = mock_faiss_repo.similarity_search(query)
    
    assert result == "Mocked error"




def test_load_chunks(mock_faiss_repo, mock_vector_store):
    chunks = [
        FileChunkEntity("Hello world 1", "metadata.txt"),
        FileChunkEntity("Hello world 2", "metadata.txt"),
        FileChunkEntity("Hello world 3", "metadata.txt"),
        FileChunkEntity("Hello world 4", "metadata.txt")
    ]

    mock_vector_store.add_documents = MagicMock(return_value="loaded")

    # Mock store_vector_store per evitare l'esecuzione reale
    with patch("repositories.faiss_repository.store_vector_store", return_value=None) as mock_store:
        result = mock_faiss_repo.load_chunks(chunks)

        # Verifica che store_vector_store sia stato chiamato
        mock_store.assert_called_once_with(mock_faiss_repo.vectorstore)

    assert result == "4 chunks loaded."


def test_load_chunks_empty_chunks(mock_faiss_repo):
    chunks = []
    
    with pytest.raises(ValueError, match="No chunks to load."):
        
        mock_faiss_repo.load_chunks(chunks)

def test_load_chunks_exception(mock_faiss_repo, mock_vector_store):
    chunks = [
        FileChunkEntity("Hello world 1", "metadata.txt"),
        FileChunkEntity("Hello world 2", "metadata.txt")
    ]

    # Simulate an exception during add_documents
    mock_vector_store.add_documents.side_effect = Exception("Mocked error during chunk loading")
    result = mock_faiss_repo.load_chunks(chunks)
    assert result == "Error occurred during chunk loading: Mocked error during chunk loading"


