import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

VECTOR_STORE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vector_store'))

def store_vector_store(vector_store: FAISS):
    """Stores the vector store to disk."""

    vector_store.save_local(VECTOR_STORE_PATH)

    print(f"Saved vector store to {VECTOR_STORE_PATH}")

def load_vector_store(embedding_model: OpenAIEmbeddings) -> FAISS:

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH, 
        embeddings=embedding_model, 
        allow_dangerous_deserialization=True # trust the data source
    )
    
    file_size = os.path.getsize(VECTOR_STORE_PATH + "/index.faiss")
    print(f"Vector store loaded from {VECTOR_STORE_PATH}")
    print(f"Size of the FAISS file: {file_size / (1024 * 1024):.2f} MB")
    print(f"Number of vectors: {vector_store.index.ntotal}")
    print(f"Dimension of vectors: {vector_store.index.d}")
    print(f"Metric type: {vector_store.index.metric_type}")

    return vector_store
        
