from dto.message_dto import MessageDTO
from usecases.get_messages_by_conversation_useCase import GetMessagesByConversationUseCase
from typing import List


class GetMessagesByConversationController:
    """
    Controller for retrieving messages by conversation from the database.
    """

    def __init__(self, get_messages_by_conversation_usecase: GetMessagesByConversationUseCase):
        self.get_messages_by_conversation_usecase = get_messages_by_conversation_usecase

    def get_messages_by_conversation(self, conversation_id: int) -> List[MessageDTO]:
        """
        Retrieve messages from the database by conversation ID.
        
        Args:
            conversation_id (int): The ID of the conversation to retrieve messages for.

        Returns:
            List[MessageDTO]: A list of data transfer objects containing message details.
        """
        try:
            result_models = self.get_messages_by_conversation_usecase.get_messages_by_conversation(conversation_id)
            
            return [
                MessageDTO(
                    id=model.id,
                    text=model.text,
                    user_id=model.user_id,
                    conversation_id=model.conversation_id,
                    rating=model.rating,
                    is_bot=model.is_bot,
                    created_at=model.created_at
                )
                for model in result_models
            ]
        except Exception as e:
            raise e
