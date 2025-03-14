import psycopg2
from app.models.support_message_model import SupportMessageModel

class SupportMessagePostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        self.__conn = conn

    def get_support_message(self, message_id: int) -> SupportMessageModel:
        with self.__conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Support WHERE id = %s", (message_id,))
            result = cursor.fetchone()
            if result:
                return SupportMessageModel(
                    id=result[0],
                    user_id=result[1],
                    description=result[2],
                    status=result[3],
                    subject=result[4],
                    created_at=result[5]
                )
            return None

    def save_support_message(self, message_id: int, content: str):
        with self.__conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE Support
                SET description = %s
                WHERE id = %s
                """,
                (content, message_id)
            )
            self.__conn.commit()