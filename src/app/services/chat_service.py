from src.app.usecases.chat_useCase import ChatUseCase

from src.app.services.similarity_search_service import SimilaritySearchService
from src.app.services.generate_answer_service import GenerateAnswerService

class ChatService(ChatUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, similarity_search_service : SimilaritySearchService, generate_answer_service : GenerateAnswerService):
        self.similarity_search_service = similarity_search_service
        self.generate_answer_service = generate_answer_service
        

    def get_answer(self, question):
        """
        Get the answer to a user's question.
        """
        return question
    
    