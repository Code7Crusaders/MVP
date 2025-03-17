from abc import ABC, abstractmethod

class SaveTemplatePort(ABC):
    """
    SaveTemplatePort is an abstract base class that defines the interface for saving templates.
    """

    @abstractmethod
    def save_template_title(self, question: str, answer: str, author: str) -> None:
        """
        Save the title of a template by question, answer, and author.
        Args:
            question (str): The question of the template.
            answer (str): The answer of the template.
            author (str): The author of the template.
        """
        