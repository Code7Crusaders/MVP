from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel

from app.ports.similarity_search_port import SimilaritySearchPort

class SimilaritySearchService:
    def __init__(self, similarity_search_port: SimilaritySearchPort):
        self.similarity_search_port = similarity_search_port

    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:

        self.similarity_search_port

        return self.similarity_search_port.similarity_search(question_model)