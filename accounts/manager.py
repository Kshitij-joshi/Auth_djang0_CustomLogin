from django.contrib.auths.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom  user model manager where email is the unique identifier
    """
    def create_user(self,email,password,**extra_fields):
        """
        create and save a User with the given email and password
        """
        if not email:
            raise ValueError("Email must be set")