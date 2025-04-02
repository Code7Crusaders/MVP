from entities.support_message_entity import SupportMessageEntity
from datetime import datetime

def test_support_message_entity_initialization():
    created_at = datetime.now()
    message = SupportMessageEntity(1, 101, "user@example.com", "Test description", True, "Test subject", created_at)
    assert message.id == 1
    assert message.user_id == 101
    assert message.user_email == "user@example.com"
    assert message.description == "Test description"
    assert message.status is True
    assert message.subject == "Test subject"
    assert message.created_at == created_at

def test_get_id():
    message = SupportMessageEntity(id=1)
    assert message.get_id() == 1

def test_get_user_id():
    message = SupportMessageEntity(user_id=101)
    assert message.get_user_id() == 101

def test_get_user_email():
    message = SupportMessageEntity(user_email="user@example.com")
    assert message.get_user_email() == "user@example.com"

def test_get_description():
    message = SupportMessageEntity(description="Test description")
    assert message.get_description() == "Test description"

def test_get_status():
    message = SupportMessageEntity(status=True)
    assert message.get_status() is True

def test_get_subject():
    message = SupportMessageEntity(subject="Test subject")
    assert message.get_subject() == "Test subject"

def test_get_created_at():
    created_at = datetime.now()
    message = SupportMessageEntity(created_at=created_at)
    assert message.get_created_at() == created_at