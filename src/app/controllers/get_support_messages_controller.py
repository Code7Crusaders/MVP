from dto.support_message_dto import SupportMessageDTO
from usecases.get_support_messages_useCase import GetSupportMessagesUseCase


class GetSupportMessagesController:
    """
    Controller for retrieving support messages from the database.
    """

    def __init__(self, get_support_messages_usecase: GetSupportMessagesUseCase):
        self.get_support_messages_usecase = get_support_messages_usecase

    def get_support_messages(self) -> list[SupportMessageDTO]:
        """
        Retrieve all support messages from the database.

        Returns:
            list[SupportMessageDTO]: A list of data transfer objects containing support message details.
        """
        try:
            result_models = self.get_support_messages_usecase.get_support_messages()
            
            return [
                SupportMessageDTO(
                    id=model.get_id(),
                    user_id=model.get_user_id(),
                    description=model.get_description(),
                    status=model.get_status(),
                    subject=model.get_subject(),
                    created_at=model.get_created_at()
                )
                for model in result_models
            ]
        
        except Exception as e:
            raise e
