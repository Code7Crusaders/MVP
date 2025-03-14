from langchain_community.vectorstores import FAISS

from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity
from app.entities.file_chunk_entity import FileChunkEntity

class FaissRepository: 
    def __init__(self, vectorstore: FAISS):
        self.vectorstore = vectorstore
        
        
    def similarity_search(self, query: QueryEntity) -> list[DocumentContextEntity]:
        """
        Performs a similarity search in the collection and returns the most relevant documents.
        
        Args:
            query (QueryEntity): The query entity containing the search parameters.
        
        Returns:
            list[DocumentContextEntity]: A list of the most relevant document context entities.
        """
        
        result = self.vectorstore.similarity_search(query.get_query(), k=4)

        context_list = []

        if not query.get_query():
            return []

        for context in result:
            context_list.append(DocumentContextEntity(context.page_content))

        return context_list

    def load_chunks(self, chunks: list[FileChunkEntity]):
        
        pass