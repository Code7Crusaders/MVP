from usecases.chat_useCase import ChatUseCase

from services.similarity_search_service import SimilaritySearchService
from services.generate_answer_service import GenerateAnswerService

from models.question_model import QuestionModel 
from models.answer_model import AnswerModel

class ChatService(ChatUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, similarity_search_service : SimilaritySearchService, generate_answer_service : GenerateAnswerService):
        self.similarity_search_service = similarity_search_service
        self.generate_answer_service = generate_answer_service
        

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
        try:
            context_list = self.similarity_search_service.similarity_search(question_model)
            answer = self.generate_answer_service.generate_answer(question_model, context_list)

            return answer
        except Exception as e:
            raise Exception(f"An error occurred during the chat response generation: {e}") from e

    