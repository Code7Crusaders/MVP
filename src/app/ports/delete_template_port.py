from abc import ABC, abstractmethod

class DeleteTemplatePort(ABC):
    """
    DeleteTemplatePort is an abstract base class that defines the interface for deleting templates.
    """

    @abstractmethod
    def delete_template(self, author: str, question: str, answer: str):
        """
        Delete a template by author, question, and answer.
        Args:
            author (str): The author of the template.
            question (str): The question of the template.
            answer (str): The answer of the template.
        """
        pass