from app.dto.support_message_dto import SupportMessageDTO
from app.usecases.get_support_message_useCase import GetSupportMessageUseCase
from app.models.support_message_model import SupportMessageModel


class GetSupportMessageController:
    """
    Controller for retrieving a support message from the database.
    """

    def __init__(self, get_support_message_usecase: GetSupportMessageUseCase):
        self.get_support_message_usecase = get_support_message_usecase

    def get_support_message(self, message_id: int) -> SupportMessageDTO:
        """
        Retrieve a support message from the database.
        
        Args:
            message_id (int): The ID of the support message to retrieve.

        Returns:
            SupportMessageDTO: The data transfer object containing support message details.
        """
        try:
            result_model = self.get_support_message_usecase.get_support_message(message_id)
            
            return SupportMessageDTO(
                id=result_model.id,
                user_id=result_model.user_id,
                description=result_model.text, 
                status=result_model.is_bot,
                subject=result_model.conversation_id,
                created_at=result_model.created_at
            )
        except Exception as e:
            raise e
