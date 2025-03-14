from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

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
        
        try:
            result = self.vectorstore.similarity_search(query.get_query(), k=4)

            context_list = []

            if not query.get_query():
                return []

            for context in result:
                context_list.append(DocumentContextEntity(context.page_content))

            return context_list
        
        except Exception as e:
            return str(e)
        

    def load_chunks(self, chunks: list[FileChunkEntity]) -> str: 
        """
        Perform a load of the chunks into the vectorstore.

        Args:
            chunks (list[FileChunkEntity]): The list of file chunk entities to load.

        Returns:
            str: The number of chunks loaded.

        Raises:
            Exception: If an error occurs during the load.
        """
        if not chunks:
            return "No chunks to load."

        try:
            result = []

            for chunk in chunks:
                doc = Document(page_content=chunk.get_chunk_content(), metadata={"metadata": chunk.get_metadata()})
                result.append(self.vectorstore.add_documents([doc]))

            return f"{len(result)} chunks loaded."

        except Exception as e:
            return f"Error occurred during chunk loading: {str(e)}"



        

       
