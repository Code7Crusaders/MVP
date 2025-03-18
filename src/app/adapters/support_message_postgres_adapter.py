from app.repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from app.models.support_message_model import SupportMessageModel
from app.ports.get_support_messages_port import GetSupportMessagePort
from app.ports.save_support_message_port import SaveSupportMessagePort

class SupportMessagePostgresAdapter(GetSupportMessagePort, SaveSupportMessagePort):

    def __init__(self, support_message_postgres_repository: SupportMessagePostgresRepository):
        self.support_message_postgres_repository = support_message_postgres_repository
    
    def get_support_message(self, message_id: int) -> SupportMessageModel:
        """
        Retrieves a support message by its ID.
        Args:
            message_id (int): The ID of the support message to retrieve.
        Returns:
            SupportMessageModel: The retrieved support message.
        """
        try:
            support_message = self.support_message_postgres_repository.get_support_message(message_id)
            return SupportMessageModel(
                id=support_message.id,
                user_id=support_message.user_id,
                description=support_message.description,
                status=support_message.status,
                subject=support_message.subject,
                created_at=support_message.created_at
            )
        except Exception as e:
            raise e

    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Retrieves all support messages.
        Returns:
            list[SupportMessageModel]: A list of support messages.
        """
        try:
            support_messages = self.support_message_postgres_repository.get_support_messages()
            return [
                SupportMessageModel(
                    id=support_message.id,
                    user_id=support_message.user_id,
                    description=support_message.description,
                    status=support_message.status,
                    subject=support_message.subject,
                    created_at=support_message.created_at
                )
                for support_message in support_messages
            ]
        except Exception as e:
            raise e
        
    def save_support_message(self, user_id: int, description: str, status: str, subject: str):
        """
        Save a support message.
        Args:
            support_message (SupportMessageModel): The support message to save.
        """
        try:
            self.support_message_postgres_repository.save_support_message(user_id, description, status, subject)
        except Exception as e:
            raise e


