from abc import ABC, abstractmethod
from models.context_model import ContextModel
from models.question_model import QuestionModel
from models.answer_model import AnswerModel
from models.prompt_template_model import PromptTemplateModel

class GenerateAnswerPort(ABC):
    """
    Interface for the generate answer port.
    """
    @abstractmethod
    def generate_answer(self, question: QuestionModel, context: list[ContextModel], prompt_template: PromptTemplateModel) -> AnswerModel:
        """
        Generates an answer based on the given question, context, and prompt template.

        Args:
            question (QuestionModel): The question model containing the user ID and question text.
            context (list[ContextModel]): A list of context models containing the context content.
            prompt_template (PromptTemplateModel): The prompt template model containing the prompt template content.

        Returns:
            AnswerModel: The generated answer model containing the answer text.
        """