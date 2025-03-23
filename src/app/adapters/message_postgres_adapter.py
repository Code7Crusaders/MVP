from repositories.message_postgres_repository import MessagePostgresRepository
from models.message_model import MessageModel
from ports.get_message_port import GetMessagePort
from ports.get_messages_by_conversation_port import GetMessagesByConversationPort
from ports.save_message_port import SaveMessagePort

from entities.message_entity import MessageEntity

class MessagePostgresAdapter(GetMessagePort, SaveMessagePort, GetMessagesByConversationPort):

    def __init__(self, message_postgres_repository: MessagePostgresRepository):
        self.message_postgres_repository = message_postgres_repository
    
    def get_message(self, message: MessageModel) -> MessageModel:
        """
        Retrieve a message by its ID.
        Args:
            message (MessageModel): The message object containing the ID to retrieve.
        Returns:
            MessageModel: The retrieved message.
        """
        try:

            message_entity = MessageEntity(
                id=message.get_id(),
                text=message.get_text(),
                created_at=message.get_created_at(),
                user_id=message.get_user_id(),
                conversation_id=message.get_conversation_id(),
                rating=message.get_rating()
            )

            message = self.message_postgres_repository.get_message(message_entity)

            return MessageModel(
                id=message.get_id(),
                text=message.get_text(),
                created_at=message.get_created_at(),
                user_id=message.get_user_id(),
                conversation_id=message.get_conversation_id(),
                rating=message.get_rating()
            )
        
        except Exception as e:
            raise e

    def get_messages_by_conversation(self, conversation: MessageModel) -> list[MessageModel]:
        """
        Retrieve messages by conversation.
        Args:
            conversation (MessageModel): The conversation object containing the ID to retrieve messages for.
        Returns:
            list[MessageModel]: A list of retrieved messages.
        """
        try:

            conversation_entity = MessageEntity(
                conversation_id=conversation.get_conversation_id()
            )

            messages = self.message_postgres_repository.get_messages_by_conversation(conversation_entity)

            return [
                MessageModel(
                    id=message.get_id(),
                    text=message.get_text(),
                    created_at=message.get_created_at(),
                    user_id=message.get_user_id(),
                    conversation_id=message.get_conversation_id(),
                    rating=message.get_rating()
                )
                for message in messages
            ]

        except Exception as e:
            raise e

    def save_message(self, message: MessageModel)-> int:
        """
        Save a message.
        Args:
            message (MessageModel): The message to save.
        Returns:
            int: The ID of the saved
        """
        try:
            message_entity = MessageEntity(
                id=message.get_id(),
                text=message.get_text(),
                created_at=message.get_created_at(),
                user_id=message.get_user_id(),
                conversation_id=message.get_conversation_id(),
                rating=message.get_rating()
            )

            return self.message_postgres_repository.save_message(message_entity)
        
        except Exception as e:
            raise e 

