from entities.user_entity import UserEntity

def test_user_entity_initialization():
    user = UserEntity(1, "testuser", "password123", "test@example.com", "1234567890", "Test", "User", True)
    assert user.id == 1
    assert user.username == "testuser"
    assert user.password == "password123"
    assert user.email == "test@example.com"
    assert user.phone == "1234567890"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.is_admin is True

def test_get_id():
    user = UserEntity(1)
    assert user.get_id() == 1

def test_get_username():
    user = UserEntity(username="testuser")
    assert user.get_username() == "testuser"

def test_get_password():
    user = UserEntity(password="password123")
    assert user.get_password() == "password123"

def test_get_email():
    user = UserEntity(email="test@example.com")
    assert user.get_email() == "test@example.com"

def test_get_phone():
    user = UserEntity(phone="1234567890")
    assert user.get_phone() == "1234567890"

def test_get_first_name():
    user = UserEntity(first_name="Test")
    assert user.get_first_name() == "Test"

def test_get_last_name():
    user = UserEntity(last_name="User")
    assert user.get_last_name() == "User"

def test_get_is_admin():
    user = UserEntity(is_admin=True)
    assert user.get_is_admin() is True