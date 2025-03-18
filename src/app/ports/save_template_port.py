from abc import ABC, abstractmethod
import app.models.template_model as TemplateModel

class SaveTemplatePort(ABC):
    """
    SaveTemplatePort is an abstract base class that defines the interface for saving templates.
    """

    @abstractmethod
    def save_template(self, question: str, answer: str, author: str) -> int:
        """
        Save a template with the provided question, answer, and author.
        Args:
            question (str): The question content of the template.
            answer (str): The answer content of the template.
            author (str): The creator of the template.
        """
        pass
        