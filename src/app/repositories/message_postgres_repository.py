import psycopg2
from app.models.message_model import MessageModel

class MessagePostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        '''
        Initializes the PostgresRepository with the given database connection.
        Args:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
        '''
        self.__conn = conn

    def get_message(self, message_id: int) -> MessageModel:
        '''
        Retrieves a message from the PostgreSQL database by its ID.
        Args:
            message_id (int): The ID of the message to retrieve.
        Returns:
            MessageModel: The retrieved message data.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the message from the PostgreSQL database.
        '''
        try:
            select_message_query = """
            SELECT id, text, created_at, user_id, conversation_id
            FROM User_Messages
            WHERE id = %s;
            """
            with self.__conn.cursor() as cursor:
                cursor.execute(select_message_query, (message_id,))
                result = cursor.fetchone()
                if result:
                    message = MessageModel(
                        id=result[0],
                        text=result[1],
                        created_at=result[2],
                        user_id=result[3],
                        conversation_id=result[4]
                    )
                    return message
                else:
                    print(f"No message found with ID {message_id}")
                    return None
        except psycopg2.Error as e:
            print(f"A connection error occurred while retrieving the message from the Postgres database: {e}")
            self.__conn.rollback()
            return None
        except Exception as e:
            print(f"An error occurred while retrieving the message from the Postgres database: {e}")
            self.__conn.rollback()
            return None

    def save_message(self, message: MessageModel):
        '''
        Saves a message into the PostgreSQL database.
        Args:
            message (MessageModel): The message data to be saved.
        Raises:
            psycopg2.Error: If an error occurs while saving the message in the PostgreSQL database.
        '''
        try:
            insert_message_query = """
            INSERT INTO User_Messages (text, created_at, user_id, conversation_id)
            VALUES (%s, %s, %s, %s);
            """
            params = (message.text, message.created_at, message.user_id, message.conversation_id)
            with self.__conn.cursor() as cursor:
                cursor.execute(insert_message_query, params)
            self.__conn.commit()
            print("Message saved successfully in the Postgres database.")
        except psycopg2.Error as e:
            print(f"A connection error occurred while saving the message in the Postgres database: {e}")
            self.__conn.rollback()
        except Exception as e:
            print(f"An error occurred while saving the message in the Postgres database: {e}")
            self.__conn.rollback()

   