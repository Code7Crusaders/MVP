from app.ports.similarity_search_port import SimilaritySearchPort
from app.ports.add_chunks_port import AddChunksPort

from app.repositories.faiss_repository import FaissRepository

from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel
from app.models.file_chunk_model import FileChunkModel

class FaissAdapter(SimilaritySearchPort, AddChunksPort):

    def __init__(self, faiss_repository: FaissRepository):
        self.faiss_repository = faiss_repository
        
    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:

        pass
    
    def load_chunks(self, chunks: list[FileChunkModel]):
        pass
    
    

