from app.entities.document_context_entity import DocumentContextEntity
from app.entities.query_entity import QueryEntity

class FaissRepository: 
    def __init__(self):
        
    def similarity_search(query: QueryEntity ) -> list[DocumentContextEntity]:
        