from app.dto.AnswerDTO import AnswerDTO
from app.dto.QuestionDTO import QuestionDTO

from app.usecases.chat_useCase import ChatUseCase

from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel

class ChatController:
    """
    Controller class to manage chat interactions.
    """
    def __init__(self, chat_usecase: ChatUseCase):
        
        try:
            self.chat_usecase = chat_usecase
        except Exception as e:
            raise e
            

    def get_answer(self, user_input: QuestionDTO) -> AnswerDTO:
        """
        Get the answer to a user's question.
        """
        # Convert DTO to model
        question_model = QuestionModel( user_input.get_user(), user_input.get_question())

        answer_dto = AnswerDTO( self.chat_usecase.get_answer(question_model) )

        # Return DTO answer
        return answer_dto
