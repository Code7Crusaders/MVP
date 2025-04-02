from models.user_model import UserModel

def test_user_model_initialization():
    user = UserModel(
        id=1,
        username="testuser",
        password="password123",
        email="testuser@example.com",
        phone="1234567890",
        first_name="Test",
        last_name="User",
        is_admin=True
    )
    assert user.get_id() == 1
    assert user.get_username() == "testuser"
    assert user.get_password() == "password123"
    assert user.get_email() == "testuser@example.com"
    assert user.get_phone() == "1234567890"
    assert user.get_first_name() == "Test"
    assert user.get_last_name() == "User"
    assert user.get_is_admin() is True

def test_user_model_default_initialization():
    user = UserModel()
    assert user.get_id() is None
    assert user.get_username() is None
    assert user.get_password() is None
    assert user.get_email() is None
    assert user.get_phone() is None
    assert user.get_first_name() is None
    assert user.get_last_name() is None
    assert user.get_is_admin() is None

def test_user_model_set_password():
    user = UserModel(password="oldpassword")
    assert user.get_password() == "oldpassword"
    user.set_password("newpassword")
    assert user.get_password() == "newpassword"