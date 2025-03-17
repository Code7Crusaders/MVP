from abc import ABC, abstractmethod
from app.models.context_model import ContextModel
from app.models.question_model import QuestionModel
from app.models.answer_model import AnswerModel
from app.models.prompt_template_model import PromptTemplateModel

class GenerateAnswerPort(ABC):
    """
    Interface for the generate answer port.
    """
    @abstractmethod
    def generate_answer(self, question: QuestionModel, context: list[ContextModel], prompt_template: PromptTemplateModel) -> AnswerModel:
        pass 