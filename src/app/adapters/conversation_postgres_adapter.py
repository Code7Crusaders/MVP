from repositories.conversation_postgres_repository import ConversationPostgresRepository
from models.conversation_model import ConversationModel

from ports.save_conversation_title_port import SaveConversationTitlePort
from ports.get_conversations_port import GetConversationsPort
from ports.get_conversation_port import GetConversationPort
from ports.delete_conversation_port import DeleteConversationPort

from entities.conversation_entity import ConversationEntity

class ConversationPostgresAdapter(GetConversationPort, GetConversationsPort, SaveConversationTitlePort, DeleteConversationPort):

    def __init__(self, conversation_postgres_repository: ConversationPostgresRepository):
        self.conversation_postgres_repository = conversation_postgres_repository
    
    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        Retrieve a conversation.
        Args:
            conversation (ConversationModel): The conversation object containing the ID to retrieve.
        Returns:
            ConversationModel: The retrieved conversation.
        """
        try:

            conversation_entity = ConversationEntity(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            ) 

            conversation = self.conversation_postgres_repository.get_conversation(conversation_entity)

            return ConversationModel(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            )
        
        except Exception as e:
            raise e

    def get_conversations(self, conversation : ConversationModel) -> list[ConversationModel]:
        """
        Retrieve all conversations.
        Returns:
            list[ConversationModel]: A list of conversations.
        """
        try:

            conversation_entity = ConversationEntity(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            )

            conversations = self.conversation_postgres_repository.get_conversations(conversation_entity)

            return [
                ConversationModel(
                    id=conversation.get_id(),
                    title=conversation.get_title(),
                    user_id=conversation.get_user_id()
                )
                for conversation in conversations
            ]
        
        except Exception as e:
            raise e

    def save_conversation_title(self, conversation: ConversationModel) -> int:
        """
        Save the title of a conversation.
        Args:
            conversation (ConversationModel): The conversation object containing the updated title.
        Returns:
            int: The ID of the saved conversation.
        """
        try:

            conversation_entity = ConversationEntity(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            )

            return self.conversation_postgres_repository.save_conversation_title(conversation_entity)

        
        except Exception as e:
            raise e

    def delete_conversation_title(self, conversation: ConversationModel) -> bool:
        """
        Delete a conversation title.
        Args:
            conversation (ConversationModel): The conversation object containing the ID to delete.
        Returns:
            int: The ID of the deleted conversation.
        """
        try:

            conversation_entity = ConversationEntity(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            )

            return self.conversation_postgres_repository.delete_conversation(conversation_entity)

        
        except Exception as e:
            raise e
