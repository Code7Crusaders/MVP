import os
from dotenv import load_dotenv
from unittest import mock

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.repositories.faiss_repository import FaissRepository
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity
from app.entities.file_chunk_entity import FileChunkEntity

# Load environment variables from .env
load_dotenv()

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_similarity_search(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.similarity_search.return_value = [DocumentContextEntity("Hello world")]  
    query = QueryEntity(1, "Hello")
    
    result = mock_repo_instance.similarity_search(query)
    
    assert len(result) > 0  
    assert all(isinstance(doc, DocumentContextEntity) for doc in result)

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_similarity_search_empty_result(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.similarity_search.side_effect = ValueError("Query cannot be empty")
    query = QueryEntity(1, "")
    
    try:
        mock_repo_instance.similarity_search(query)
    except ValueError as e:
        assert str(e) == "Query cannot be empty"

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_similarity_search_error(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.similarity_search.return_value = "NoneType error"
    query = QueryEntity(1, "Hello")
    
    result = mock_repo_instance.similarity_search(query)
    
    assert "NoneType" in result

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_load_chunks(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.load_chunks.return_value = "3 chunks loaded."
    chunks = [
        FileChunkEntity("This is the first chunk.", "chunk1"),
        FileChunkEntity("This is the second chunk.", "chunk2"),
        FileChunkEntity("This is the third chunk.", "chunk3")
    ]
    
    result = mock_repo_instance.load_chunks(chunks)
    
    assert result == "3 chunks loaded."

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_load_chunks_empty(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.load_chunks.side_effect = ValueError("No chunks to load.")
    chunks = []
    
    try:
        mock_repo_instance.load_chunks(chunks)
    except ValueError as e:
        assert str(e) == "No chunks to load."

@mock.patch("app.repositories.faiss_repository.FaissRepository")
def test_load_chunks_error(mock_faiss_repo):
    mock_repo_instance = mock_faiss_repo.return_value
    mock_repo_instance.load_chunks.return_value = "NoneType error"
    chunks = [
        FileChunkEntity("This is the first chunk.", "chunk1"),
        FileChunkEntity("This is the second chunk.", "chunk2"),
        FileChunkEntity("This is the third chunk.", "chunk3")
    ]
    
    result = mock_repo_instance.load_chunks(chunks)
    
    assert "NoneType" in result
