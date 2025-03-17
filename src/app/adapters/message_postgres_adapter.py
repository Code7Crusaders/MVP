from app.repositories.message_postgres_repository import MessagePostgresRepository
from app.models.message_model import MessageModel
from app.ports.get_message_port import GetMessagePort
from app.ports.get_messages_by_conversation import GetMessagesByConversationPort
from app.ports.save_message_port import SaveMessageTitlePort

class messagePostgresAdapter(GetMessagePort, SaveMessageTitlePort, GetMessagesByConversationPort):

    def __init__(self, message_postgres_repository: MessagePostgresRepository):
        self.message_postgres_repository = message_postgres_repository
    
    def get_message(self, message_id: int) -> MessageModel:
        """
        Retrieve a message by its ID.
        Args:
            message_id (int): The ID of the message to retrieve.
        Returns:
            messageModel: The retrieved message.
        """
        try:
            message = self.message_postgres_repository.get_message(message_id)
            return MessageModel(
                id=message.id,
                text=message.text,
                created_at=message.created_at,
                user_id=message.user_id,
                conversation_id=message.conversation_id,
                rating=message.rating
            )
        except Exception as e:
            raise e

    def get_messages_by_conversation(self, conversation_id: int) -> list[MessageModel]:
        """
        Save a message.
        Args:
            message_id (int): The ID of the message.
            title (str): The new title of the message.
        """
        try:
            self.message_postgres_repository.save_message_title(conversation_id)
        except Exception as e:
            raise e

    def save_message(self, message: MessageModel):
        """
        Save a message.
        Args:
            message (MessageModel): The message to save.
        """
        try:
            self.message_postgres_repository.save_message(message)
        except Exception as e:
            raise e 

