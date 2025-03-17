from dto.AnswerDTO import AnswerDTO
from dto.QuestionDTO import QuestionDTO

from usecases.chat_useCase import ChatUseCase

from models.question_model import QuestionModel
from models.answer_model import AnswerModel

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
        Retrieves an answer based on the user's question.

        Args:
            user_input (QuestionDTO): The user's input question.

        Returns:
            AnswerDTO: The generated answer based on the retrieved context.
                    
        """
        try:
            question_model = QuestionModel( user_input.get_user(), user_input.get_question())

            answer_model = self.chat_usecase.get_answer(question_model)

            answer_dto = AnswerDTO( answer_model.get_answer() )

            return answer_dto
        
        except Exception as e:
            raise e
