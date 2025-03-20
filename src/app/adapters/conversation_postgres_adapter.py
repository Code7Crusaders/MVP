from app.repositories.conversation_postgres_repository import ConversationPostgresRepository
from app.models.conversation_model import ConversationModel
from app.ports.save_conversation_title_port import SaveConversationTitlePort
from app.ports.get_conversation_port import GetConversationPort

class ConversationPostgresAdapter(GetConversationPort, SaveConversationTitlePort):

    def __init__(self, conversation_postgres_repository: ConversationPostgresRepository):
        self.conversation_postgres_repository = conversation_postgres_repository
    
    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        Retrieve a conversation by its ID.
        Args:
            conversation_id (int): The ID of the conversation to retrieve.
        Returns:
            ConversationModel: The retrieved conversation.
        """
        try:
            conversation = self.conversation_postgres_repository.get_conversation(conversation.get_id())
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
                    id=conversation.id,
                    title=conversation.title,
                )
                for conversation in conversations
            ]
        except Exception as e:
            raise e

    def save_conversation_title(self, conversation: ConversationModel) -> bool:
        """
        Save the title of a conversation.
        Args:
            conversation_id (int): The ID of the conversation.
            title (str): The new title of the conversation.
        """
        try:
            self.conversation_postgres_repository.save_conversation_title(conversation)
        except Exception as e:
            raise e


