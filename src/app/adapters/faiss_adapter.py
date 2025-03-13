from app.ports.similarity_search_port import SimilaritySearchPort

from app.repositories.faiss_repository import FaissRepository

from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel

class FaissAdapter(SimilaritySearchPort):

    def __init__(self, faiss_repository: FaissRepository):
        self.faiss_repository = faiss_repository
        
    def similarity_search(question_model: QuestionModel) -> list[ContextModel]:
        