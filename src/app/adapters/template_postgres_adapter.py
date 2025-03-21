from app.repositories.template_postgres_repository import TemplatePostgresRepository
from app.models.template_model import TemplateModel
from app.ports.get_template_port import GetTemplatePort
from app.ports.get_template_list_port import GetTemplateListPort
from app.ports.save_template_port import SaveTemplatePort
from app.ports.delete_template_port import DeleteTemplatePort

from entities.template_entity import TemplateEntity


class TemplatePostgresAdapter(GetTemplatePort, GetTemplateListPort, SaveTemplatePort, DeleteTemplatePort):

    def __init__(self, template_postgres_repository: TemplatePostgresRepository):
        self.template_postgres_repository = template_postgres_repository
    
    def get_template(self, template: TemplateModel) -> TemplateModel:
        """
        Retrieve a template by its details.
        Args:
            template (TemplateModel): The template details to retrieve.
        Returns:
            TemplateModel: The retrieved template.
        """
        try:

            template_entity = TemplateEntity(
                id=template.get_id(),
                question=template.get_question(),
                answer=template.get_answer(),
                author_id=template.get_author_id(),
                last_modified=template.get_last_modified()
            )

            template = self.template_postgres_repository.get_template(template_entity)

            return TemplateModel(
                id=template.get_id(),
                question=template.get_question(),
                answer=template.get_answer(),
                author_id=template.get_author_id(),
                last_modified=template.get_last_modified()
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

            return [ 
                TemplateModel(
                    id=template.get_id(),
                    question=template.get_question(),
                    answer=template.get_answer(),
                    author_id=template.get_author_id(),
                    last_modified=template.get_last_modified()
                )
                for template in templates
            ]
        
        except Exception as e:
            raise e
        
    def save_template(self, template: TemplateModel) -> int:
        """
        Save a template.
        Args:
            template (TemplateModel): The template to save.
        Returns:
            int: The ID of the saved template.
        """
        try:

            template_entity = TemplateEntity(
                id=template.get_id(),
                question=template.get_question(),
                answer=template.get_answer(),
                author_id=template.get_author_id(),
                last_modified=template.get_last_modified()
            )

            return self.template_postgres_repository.save_template_title(template_entity)
            
        except Exception as e:
            raise e


    def delete_template(self, template: TemplateModel) -> bool:
        """
        Delete a template.
        Args:
            template (TemplateModel): The template to delete.
        Returns:
            bool: True if the template was deleted successfully, otherwise False.
        """
        try:
            
            template_entity = TemplateEntity(
                id=template.get_id(),
                question=template.get_question(),
                answer=template.get_answer(),
                author_id=template.get_author_id(),
                last_modified=template.get_last_modified()
            )

            return self.template_postgres_repository.delete_template(template_entity)

        except Exception as e:
            raise e

