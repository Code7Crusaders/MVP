from abc import ABC, abstractmethod
from app.models.context_model import ContextModel
from app.models.question_model import QuestionModel

class SimilaritySearchPort(ABC):
    """
    Interface for the similarity search port.
    """
    @abstractmethod
    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:
        pass 