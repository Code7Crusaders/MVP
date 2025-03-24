

class UserDTO:

    def __init__(self, id: int = None, username: str = None, password: str = None, email: str = None, phone: str = None, first_name: str = None, last_name: str = None, is_admin: bool = None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin

    def get_id(self) -> int: 
        return self.id
        
    def get_username(self) -> str:
        return self.username
        
    def get_password(self) -> str:
        return self.password
        
    def set_password(self, password: str) -> None:
        self.password = password

    def get_email(self) -> str:
        return self.email
        
    def get_phone(self) -> str:
        return self.phone
        
    def get_first_name(self) -> str:
        return self.first_name
        
    def get_last_name(self) -> str:
        return self.last_name
        
    def get_is_admin(self) -> bool:
        return self.is_admin
        