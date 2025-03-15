import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.repositories.message_postgres_repository import MessagePostgresRepository
from app.config.db_config import db_config
from app.entities.message_entity import MessageEntity
from datetime import datetime

def test_get_message():
    repo = MessagePostgresRepository(db_config)
    message = repo.get_message(30)
    if message:
        print(f"message ID: {message.id}, Title: {message.text}")
    else:
        print("message not found.")

def test_save_message():
    repo = MessagePostgresRepository(db_config)
    message = MessageEntity(
        id=None,
        text="Hello World",
        created_at=datetime.now(),
        user_id=1,
        conversation_id=1,
        rating=False
    )
    repo.save_message(message)
    print("message saved.")

def test_get_messages_by_conversation():
    repo = MessagePostgresRepository(db_config)
    messages = repo.get_messages_by_conversation(1)
    for message in messages:
        print(f"message ID: {message.id}, Text: {message.text}")

if __name__ == "__main__":
    #test_save_message()
    #test_get_message()
    test_get_messages_by_conversation()

#funziona