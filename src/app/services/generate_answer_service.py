from models.answer_model import AnswerModel
from models.question_model import QuestionModel
from models.context_model import ContextModel
from models.prompt_template_model import PromptTemplateModel

from ports.generate_answer_port import GenerateAnswerPort

class GenerateAnswerService:
    """
    Service class to generate answer basing on a query and a list of contexts."
    """
    def __init__(self, generate_answer_port: GenerateAnswerPort, prompt_template_model: PromptTemplateModel):
        self.generate_answer_port = generate_answer_port
        self.prompt_template_model = prompt_template_model
        

    def generate_answer(self, question_model: QuestionModel, context: list[ContextModel]) -> AnswerModel:
        """
        Generates an answer based on user input and relevant documents.

        Args:
            question_model (QuestionModel): The user's input question.
            context (list[ContextModel]): The relevant documents.

        Returns:
            AnswerModel: The generated answer.

        Raises:
            ValueError: raises exeptions.
        """
        try:

            return self.generate_answer_port.generate_answer(question_model, context, self.prompt_template_model)
        
        except Exception as e:
            raise Exception(f"An error occurred during the answer generation: {e}") from e
        