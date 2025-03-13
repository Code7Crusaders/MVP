from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity

class FaissRepository: 
    def __init__(self):
        pass
        
    def similarity_search(self, query: QueryEntity ) -> list[DocumentContextEntity]:

        pass