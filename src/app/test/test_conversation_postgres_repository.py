import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.repositories.conversation_postgres_repository import ConversationPostgresRepository
from app.config.db_config import db_config

def test_get_conversation():
    repo = ConversationPostgresRepository(db_config)
    conversation = repo.get_conversation(1)
    if conversation:
        print(f"Conversation ID: {conversation.id}, Title: {conversation.title}")
    else:
        print("Conversation not found.")

def test_save_conversation_title():
    repo = ConversationPostgresRepository(db_config)
    repo.save_conversation_title(1, "New Title")
    print("Conversation title updated.")

if __name__ == "__main__":
    test_save_conversation_title()
    test_get_conversation()


# funziona
