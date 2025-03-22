from abc import ABC, abstractmethod
from models.context_model import ContextModel
from models.question_model import QuestionModel

class SimilaritySearchPort(ABC):
    """
    Interface for the similarity search port.
    """
    @abstractmethod
    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:
        """
        Perform a similarity search using the provided question model.

        Args:
            question_model (QuestionModel): The model containing the question to search for.

        Returns:
            list[ContextModel]: A list of context models that are similar to the question.
        """