from datetime import datetime
from dto.support_message_dto import SupportMessageDTO

def test_support_message_dto_initialization():
    created_at = datetime.now()
    message = SupportMessageDTO(
        id=1,
        user_id=101,
        user_email="user@example.com",
        description="This is a test message.",
        status=True,
        subject="Test Subject",
        created_at=created_at
    )
    assert message.get_id() == 1
    assert message.get_user_id() == 101
    assert message.get_user_email() == "user@example.com"
    assert message.get_description() == "This is a test message."
    assert message.get_status() is True
    assert message.get_subject() == "Test Subject"
    assert message.get_created_at() == created_at

def test_support_message_dto_default_initialization():
    message = SupportMessageDTO()
    assert message.get_id() is None
    assert message.get_user_id() is None
    assert message.get_user_email() is None
    assert message.get_description() is None
    assert message.get_status() is None
    assert message.get_subject() is None
    assert message.get_created_at() is None