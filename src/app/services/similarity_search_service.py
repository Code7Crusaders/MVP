from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel

from app.ports.similarity_search_port import SimilaritySearchPort

class SimilaritySearchService:
    def __init__(self, similarity_search_port: SimilaritySearchPort):
        self.similarity_search_port = similarity_search_port

    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:
        """
        This function manages the logic for getting the most similar documents stored in the vector DB
        for the given query.
        """
        return self.similarity_search_port.similarity_search(question_model)