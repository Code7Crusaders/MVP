from app.models.answer_model import AnswerModel
from app.models.question_model import QuestionModel

class GenerateAnswerService:
    """
    Service class to generate answer basing on a query"
    """
    def generate_answer(self, question_model : QuestionModel, context : list<ContextModel>) -> AnswerModel:
        """
        Generate an answer to a user's question.
        """
        return question