from repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from models.support_message_model import SupportMessageModel
from ports.get_support_message_port import GetSupportMessagePort
from ports.get_support_messages_port import GetSupportMessagesPort
from ports.save_support_message_port import SaveSupportMessagePort

from entities.support_message_entity import SupportMessageEntity

class SupportMessagePostgresAdapter(GetSupportMessagePort, GetSupportMessagesPort, SaveSupportMessagePort):

    def __init__(self, support_message_postgres_repository: SupportMessagePostgresRepository):
        self.support_message_postgres_repository = support_message_postgres_repository
    
    def get_support_message(self, message: SupportMessageModel) -> SupportMessageModel:
        """
        Retrieves a support message.
        Args:
            message (SupportMessageModel): The support message model containing the details.
        Returns:
            SupportMessageModel: The retrieved support message.
        """

        try:
            support_message_entity = SupportMessageEntity(
                id=message.get_id(),
                user_id=message.get_user_id(),
                description=message.get_description(),
                status=message.get_status(),
                subject=message.get_subject(),
                created_at=message.get_created_at()
            )

            support_message = self.support_message_postgres_repository.get_support_message(support_message_entity)

            return SupportMessageModel(
                id=support_message.get_id(),
                user_id=support_message.get_user_id(),
                description=support_message.get_description(),
                status=support_message.get_status(),
                subject=support_message.get_subject(),
                created_at=support_message.get_created_at()
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
        
    def save_support_message(self, support_message: SupportMessageModel)-> int:
        """
        Save a support message.
        Args:
            support_message (SupportMessageModel): The support message to save.
        Returns:
            int: The ID of the saved support message.
        """
        try:

            support_message_entity = SupportMessageEntity(
                id=support_message.get_id(),
                user_id=support_message.get_user_id(),
                description=support_message.get_description(),
                status=support_message.get_status(),
                subject=support_message.get_subject(),
                created_at=support_message.get_created_at()
            )

            return self.support_message_postgres_repository.save_support_message(support_message_entity)

        
        except Exception as e:
            raise e
