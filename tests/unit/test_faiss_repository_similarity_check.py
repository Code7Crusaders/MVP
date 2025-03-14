import pytest
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.repositories.faiss_repository import FaissRepository
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity

# Load environment variables from .env
load_dotenv()

@pytest.fixture
def faiss_repository():
    # Read API key from .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    # Initialize OpenAI embedding model
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)

    # Create FAISS vector store with sample documents
    texts = ["Hello world", "How are you?", "Goodbye!", "Nice to meet you"]
    vector_store = FAISS.from_texts(texts, embedding_model)

    return FaissRepository(vector_store)

def test_similarity_search(faiss_repository):
    query = QueryEntity(1, "Hello")

    result = faiss_repository.similarity_search(query)

    assert len(result) > 0  # Ensure at least one result
    assert all(isinstance(doc, DocumentContextEntity) for doc in result)

    print("\nSimilarity Search Results:")
    for doc in result:
        print(doc.get_content())

def test_similarity_search_empty_result(faiss_repository):
    query = QueryEntity(1, "")

    result = faiss_repository.similarity_search(query)

    assert len(result) == 0  # Ensure no irrelevant matches
