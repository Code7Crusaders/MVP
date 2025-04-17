from abc import ABC, abstractmethod
from models.question_model import QuestionModel
from models.answer_model import AnswerModel

class ChatUseCase(ABC):

    @abstractmethod
    def get_answer(self, question_model : QuestionModel) -> AnswerModel:
        """
        Retrieves an answer based on the user's question.

        Args:
            question_model (QuestionModel): The user's input question.

        Returns:
            AnswerModel: The generated answer based on the retrieved context.

        Raises:
            Exception: If an error occurs during the similarity search or answer generation.
        """


