from app.usecases.chat_useCase import ChatUseCase

from app.services.similarity_search_service import SimilaritySearchService
from app.services.generate_answer_service import GenerateAnswerService

from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel

class ChatService(ChatUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, similarity_search_service : SimilaritySearchService, generate_answer_service : GenerateAnswerService):
        self.similarity_search_service = similarity_search_service
        self.generate_answer_service = generate_answer_service
        

    def get_answer(self, question_model : QuestionModel) -> AnswerModel:
        """
        Get the answer to a user's question.
        """
        context_list = self.similarity_search_service.similarity_search(question_model)
        answer = self.generate_answer_service.generate_answer(question_model, context_list)

        return answer
    
    