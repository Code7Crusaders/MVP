from app.repositories.template_postgres_repository import TemplatePostgresRepository
from app.models.template_model import TemplateModel
from app.ports.get_template_port import GetTemplatePort
from app.ports.get_template_list_port import GetTemplateListPort
from app.ports.save_template_port import SaveTemplatePort
from app.ports.delete_template_port import DeleteTemplatePort


class TemplatePostgresAdapter(GetTemplatePort, GetTemplateListPort, SaveTemplatePort, DeleteTemplatePort):

    def __init__(self, template_postgres_repository: TemplatePostgresRepository):
        self.template_postgres_repository = template_postgres_repository
    
    def get_template(self, template_id: int) -> TemplateModel:
        """
        Retrieve a template by its ID.
        Args:
            template_id (int): The ID of the template to retrieve.
        Returns:
            templateModel: The retrieved template.
        """
        try:
            template = self.template_postgres_repository.get_template(template_id)
            return TemplateModel(
                question=template.question,
                answer=template.answer,
                author=template.author,
            )
        except Exception as e:
            raise e


    def get_template_list(self) -> list[TemplateModel]: 
        """
        Retrieve all templates.
        Returns:
            list[TemplateModel]: A list of TemplateModel objects.
        """
        try:
            templates = self.template_postgres_repository.get_template_list()
            return [TemplateModel(question=template.question, answer=template.answer, author=template.author) for template in templates]
        except Exception as e:
            raise e
        
    def save_template_title(self, template_id: int, title: str):
        """
        Save the title of a template.
        Args:
            template_id (int): The ID of the template.
            title (str): The new title of the template.
        """
        try:
            self.template_postgres_repository.save_template_title(template_id, title)
        except Exception as e:
            raise e

    def delete_template(self, author: str, question: str, answer: str):
        """
        Delete a template.
        Args:
            author (str): The author of the template.
            question (str): The question of the template.
            answer (str): The answer of the template.
        """
        try:
            self.template_postgres_repository.delete_template(author, question, answer)
        except Exception as e:
            raise e

