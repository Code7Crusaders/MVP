import psycopg2
from app.models.message_model import MessageModel
from app.models.conversation_model import ConversationModel
from app.models.user_model import UserModel
from app.models.feedback_model import FeedbackModel
from app.models.support_message_model import SupportMessageModel
from app.models.template_model import TemplateModel

class PostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        '''
        Initializes the PostgresRepository with the given database connection.
        Args:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
        '''
        self.__conn = conn

    def get_message(self, message_id: int) -> MessageModel:
        # Implementation here
        pass

    def get_conversation(self, conversation_id: int) -> ConversationModel:
        # Implementation here
        pass

    def save_conversation_title(self, conversation_id: int, conversation_title: str):
        # Implementation here
        pass

    def save_message(self, message: MessageModel):
        # Implementation here
        pass

    def login(self, username: str, password: str) -> UserModel:
        # Implementation here
        pass

    def register(self, user: UserModel):
        # Implementation here
        pass

    def get_feedback(self, message_id: int) -> FeedbackModel:
        # Implementation here
        pass

    def save_feedback(self, feedback: FeedbackModel):
        # Implementation here
        pass

    def get_support_messages(self) -> List[SupportMessageModel]:
        # Implementation here
        pass

    def save_support_message(self, support_message: SupportMessageModel):
        # Implementation here
        pass

    def get_template_list(self) -> list[TemplateModel]:
        # Implementation here
        pass

    def get_random_template(self) -> TemplateModel:
        # Implementation here
        pass

    def save_template(self, template: TemplateModel):
        # Implementation here
        pass