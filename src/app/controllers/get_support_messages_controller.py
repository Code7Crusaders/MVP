from app.dto.support_message_dto import SupportMessageDTO
from app.usecases.get_support_messages_useCase import GetSupportMessagesUseCase


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
                    id=model.id,
                    user_id=model.user_id,
                    description=model.text,
                    status=model.is_bot,
                    subject=model.conversation_id,
                    created_at=model.created_at
                )
                for model in result_models
            ]
        except Exception as e:
            raise e
