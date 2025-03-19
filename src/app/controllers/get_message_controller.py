from dto.message_dto import MessageDTO
from usecases.get_message_useCase import GetMessageUseCase
from models.message_model import MessageModel


class GetMessageController:
    """
    Controller for retrieving a message from the database.
    """

    def __init__(self, get_message_usecase: GetMessageUseCase):
        
        self.get_message_usecase = get_message_usecase

    def get_message(self, message_id: int) -> MessageDTO:
        """
        Retrieve a message from the database.
        
        Args:
            message_id (int): The ID of the message to retrieve.

        Returns:
            MessageDTO: The data transfer object containing message details.
        """
        try:
            result_model = self.get_message_usecase.get_message(message_id)
            
            return MessageDTO(
                id=result_model.id,
                text=result_model.text,
                user_id=result_model.user_id,
                conversation_id=result_model.conversation_id,
                rating=result_model.rating,
                is_bot=result_model.is_bot,
                created_at=result_model.created_at
            )
        except Exception as e:
            raise e
