import pytest
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.repositories.faiss_repository import FaissRepository
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity
from app.entities.file_chunk_entity import FileChunkEntity

# Load environment variables from .env
load_dotenv()

@pytest.fixture
def faiss_repository():
    # Read API key from .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    # OpenAI embedding model
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)

    # Create FAISS vector store with sample documents
    texts = ["Hello world", "How are you?", "Goodbye!", "Nice to meet you"]
    vector_store = FAISS.from_texts(texts, embedding_model)

    return FaissRepository(vector_store)

def test_similarity_search(faiss_repository):
    query = QueryEntity(1, "Hello")

    result = faiss_repository.similarity_search(query)

    assert len(result) > 0  
    assert all(isinstance(doc, DocumentContextEntity) for doc in result)

def test_similarity_search_empty_result(faiss_repository):
    query = QueryEntity(1, "")

    result = faiss_repository.similarity_search(query)

    assert len(result) == 0  

def test_similarity_search_error(faiss_repository):
    query = QueryEntity(1, "Hello")

    # Remove vector store to simulate error
    faiss_repository.vectorstore = None

    result = faiss_repository.similarity_search(query)

    assert "NoneType" in result

def test_load_chunks(faiss_repository):
    chunks = [
        FileChunkEntity("This is the first chunk." , "chunk1"),
        FileChunkEntity("This is the second chunk." , "chunk2"),
        FileChunkEntity("This is the third chunk." , "chunk3")
    ]

    result = faiss_repository.load_chunks(chunks)
    
    assert result == "3 chunks loaded."  

def test_load_chunks_empty(faiss_repository):
    chunks = []
    result = faiss_repository.load_chunks(chunks)
    
    assert result == "No chunks to load."  

def test_load_chunks_error(faiss_repository):
    chunks = [
        FileChunkEntity("This is the first chunk." , "chunk1"),
        FileChunkEntity("This is the second chunk." , "chunk2"),
        FileChunkEntity("This is the third chunk." , "chunk3")
    ]

    # Remove vector store to simulate error
    faiss_repository.vectorstore = None

    result = faiss_repository.load_chunks(chunks)
    

    assert "NoneType" in result 
