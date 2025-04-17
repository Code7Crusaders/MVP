from abc import ABC, abstractmethod

class ValidationPort(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> bool:
        """
        Get a user by email.
        
        Args:
            email (str): The email of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """


    @abstractmethod
    def get_user_by_username(self, username: str) -> bool:
        """
        Get a user by username.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """