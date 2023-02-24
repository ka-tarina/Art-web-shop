"""Module for superuser service."""
import hashlib

from app.db.database import SessionLocal
from app.users.repository import SuperUserRepository


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = SuperUserRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class SuperUserServices:
    """A service class for SuperUser models."""
    @staticmethod
    @repository_method_wrapper
    def create_superuser(repository, username, email, password):
        """Creates a new superuser in the system."""
        hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        return repository.create_superuser(username=username, email=email, password=hashed_password)

    @staticmethod
    @repository_method_wrapper
    def create_superuser_from_existing_user(repository, user_id):
        """Creates a new superuser in the system from existing user."""
        return repository.create_superuser_from_existing_user(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_superuser_by_id(repository, superuser_id):
        """Gets a superuser from the database by their ID."""
        return repository.get_superuser_by_id(superuser_id=superuser_id)

    @staticmethod
    @repository_method_wrapper
    def get_all_superusers(repository):
        """Gets all superusers from the database."""
        return repository.get_all_superusers()

    @staticmethod
    @repository_method_wrapper
    def delete_superuser_by_id(repository, superuser_id: str):
        """Deletes a superuser from the database by their ID."""
        return repository.delete_superuser_by_id(superuser_id=superuser_id)
