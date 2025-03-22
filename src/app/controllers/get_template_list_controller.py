from usecases.get_template_list_useCase import GetTemplateListUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

class GetTemplateListController:

    def __init__(self, get_template_list_use_case: GetTemplateListUseCase):
        self.get_template_list_use_case = get_template_list_use_case

    def get_template_list(self) -> list[TemplateDTO]:
        """
        Get all templates from the database.
        Returns:
            list[TemplateDTO]: A list of templates retrieved from the database.
        """
        try:
            
            templates_result = self.get_template_list_use_case.get_template_list()

            return [
                TemplateDTO(
                    id=template.get_id(),
                    question=template.get_question(),
                    answer=template.get_answer(),
                    author_id=template.get_author_id(),
                    last_modified=template.get_last_modified()
                )
                for template in templates_result
            ]

        except Exception as e:
            raise e