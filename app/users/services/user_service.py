"""Module for user service"""
import hashlib
from pydantic import EmailStr
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.enums import UserStatus
from app.users.repository import UserRepository


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = UserRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class UserServices:
    """A service class for User models."""
    @staticmethod
    @repository_method_wrapper
    def create_user(repository, username, email, password: str):
        """Creates a new user in the system."""
        hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        return repository.create_user(username=username, email=email, password=hashed_password)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_id(repository, user_id: str):
        """Gets a user from the database by their ID."""
        return repository.get_user_by_id(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username(repository, username: str):
        """Gets a user from the database by their username."""
        return repository.get_user_by_username(username=username)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username_or_id(repository, username_or_id: str):
        """Gets a user from the database by their username or their ID."""
        return repository.get_user_by_username_or_id(username_or_id=username_or_id)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_email(repository, email: EmailStr):
        """Gets a user from the database by their email."""
        return repository.read_user_by_email(email=email)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username_or_id_or_email(repository, username_id_email: str):
        """Gets a user from the database by either their username, ID or email."""
        return repository.get_user_by_username_or_id_or_email(username_id_email=username_id_email)

    @staticmethod
    @repository_method_wrapper
    def update_user_email(repository, email: EmailStr, new_email: EmailStr):
        """Updates the email of the user."""
        return repository.update_user_email(email=email, new_email=new_email)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Verifies the user password"""
        return hashed_password == hashlib.sha256(bytes(plain_password, "utf-8")).hexdigest()

    @staticmethod
    @repository_method_wrapper
    def update_user_password(repository, email: EmailStr, password: str, new_password: str):
        """Updates the password of the user."""
        user = repository.read_user_by_email(email=email)
        if not repository.check_password(user_id=user.email, password=password):
            raise ValueError("Invalid old password")
        hashed_password = hashlib.sha256(bytes(new_password, 'utf-8')).hexdigest()
        return repository.update_user_password(email=email, new_password=hashed_password)

    @staticmethod
    @repository_method_wrapper
    def update_user_status(repository, username_id_email: str, status: UserStatus):
        """Updates the status of the user."""
        return repository.update_user_status(username_id_email=username_id_email, status=status)

    @staticmethod
    @repository_method_wrapper
    def update_user_role(repository, username_id_email: str, role: UserStatus):
        """Updates the role of the user."""
        return repository.update_user_role(username_id_email=username_id_email, role=role)

    @staticmethod
    @repository_method_wrapper
    def get_all_users(repository):
        """Gets all users from the database."""
        return repository.get_all_users()

    @staticmethod
    @repository_method_wrapper
    def delete_user_by_id(repository, user_id: str):
        """Deletes a user from the database by their ID."""
        return repository.delete_user_by_id(user_id=user_id)

    @staticmethod
    def login_user(email: EmailStr, password: str):
        """Logs user in the system."""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email=email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
