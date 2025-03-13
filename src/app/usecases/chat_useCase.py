from abc import ABC, abstractmethod
from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel

class ChatUseCase(ABC):

    @abstractmethod
    def get_answer(self, question : QuestionModel) -> AnswerModel:
        pass


