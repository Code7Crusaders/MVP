from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity
from app.entities.file_chunk_entity import FileChunkEntity

class FaissRepository: 
    def __init__(self):
        
        pass
        
    def similarity_search(self, query: QueryEntity ) -> list[DocumentContextEntity]:

        pass

    def load_chunks(self, chunks: list[FileChunkEntity]):
        
        pass