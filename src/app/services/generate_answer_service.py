from app.models.answer_model import AnswerModel
from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel

class GenerateAnswerService:
    """
    Service class to generate answer basing on a query and a list of contexts."
    """
    def generate_answer(self, question_model: QuestionModel, context: list[ContextModel]) -> AnswerModel:
        pass
        