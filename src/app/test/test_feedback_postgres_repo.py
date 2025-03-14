import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.repositories.feedback_postgres_repository import FeedbackPostgresRepository
from app.config.db_config import db_config

def test_get_feedback():
    repo = FeedbackPostgresRepository(db_config)
    feedback = repo.get_feedback(1)
    if feedback:
        print(f"Feedback ID: {feedback.id}, Content: {feedback.content}")
    else:
        print("Feedback not found.")

def test_save_feedback():
    repo = FeedbackPostgresRepository(db_config)
    repo.save_feedback(1, "New Feedback Content")
    print("Feedback content updated.")

if __name__ == "__main__":
    test_save_feedback()
    test_get_feedback()

# funziona
