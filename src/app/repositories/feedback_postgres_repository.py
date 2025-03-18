import psycopg2
from models.feedback_model import FeedbackModel

class FeedbackPostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        '''
        Initializes the PostgresRepository with the given database connection.
        Args:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
        '''
        self.__conn = conn

    def get_feedback(self, message_id: int) -> FeedbackModel:
        with self.__conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Support WHERE id = %s", (message_id,))
            result = cursor.fetchone()
            if result:
                return FeedbackModel(
                    id=result[0],
                    user_id=result[1],
                    description=result[2],
                    status=result[3],
                    subject=result[4],
                    created_at=result[5]
                )
            return None

    def save_feedback(self, feedback: FeedbackModel):
        with self.__conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO Support (user_id, description, status, subject)
                VALUES (%s, %s, %s, %s)
                RETURNING id, created_at
                """,
                (feedback.user_id, feedback.description, feedback.status, feedback.subject)
            )
            self.__conn.commit()
            result = cursor.fetchone()
            feedback.id = result[0]
            feedback.created_at = result[1]