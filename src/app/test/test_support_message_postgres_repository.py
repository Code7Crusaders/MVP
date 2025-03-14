import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from app.config.db_config import db_config

def test_get_support_message():
    repo = SupportMessagePostgresRepository(db_config)
    support_message = repo.get_support_message(1)
    if support_message:
        print(f"Support Message ID: {support_message.id}, User ID: {support_message.user_id}, Description: {support_message.description}, Status: {support_message.status}, Subject: {support_message.subject}, Created At: {support_message.created_at}")
    else:
        print("Support message not found.")

def test_save_support_message():
    repo = SupportMessagePostgresRepository(db_config)
    new_message_id = repo.save_support_message(1, "New Support Message Content", "true", "New Subject")
    print(f"New support message created with ID: {new_message_id}")

if __name__ == "__main__":
    test_save_support_message()
    test_get_support_message()
