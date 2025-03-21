from repositories.conversation_postgres_repository import ConversationPostgresRepository
from models.conversation_model import ConversationModel
from ports.save_conversation_title_port import SaveConversationTitlePort
from ports.get_conversation_port import GetConversationPort

from entities.conversation_entity import ConversationEntity

class ConversationPostgresAdapter(GetConversationPort, SaveConversationTitlePort):

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
            ) 

            conversation = self.conversation_postgres_repository.get_conversation(conversation_entity)

            return ConversationModel(
                id=conversation.get_id(),
                title=conversation.get_title(),
            )
        
        except Exception as e:
            raise e

    def get_conversations(self) -> list[ConversationModel]:
        """
        Retrieve all conversations.
        Returns:
            list[ConversationModel]: A list of conversations.
        """
        try:

            conversations = self.conversation_postgres_repository.get_conversations()

            return [
                ConversationModel(
                    id=conversation.get_id(),
                    title=conversation.get_title(),
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
            )

            return self.conversation_postgres_repository.save_conversation_title(conversation_entity)

        
        except Exception as e:
            raise e


