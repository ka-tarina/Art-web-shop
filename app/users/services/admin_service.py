"""Module for admin service."""
import hashlib

from pydantic import EmailStr

from app.db.database import SessionLocal
from app.users.repository import AdminRepository, UserRepository


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = AdminRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e

    return wrapper


class AdminServices:
    """A service class for Admin models."""
    @staticmethod
    @repository_method_wrapper
    def create_admin(repository, username, email, password):
        """Creates a new admin in the system."""
        hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        return repository.create_admin(
            username=username, email=email, password=hashed_password
        )

    @staticmethod
    @repository_method_wrapper
    def create_admin_from_existing_user(repository, user_id):
        """Creates a new admin in the system from existing user."""
        return repository.create_admin_from_existing_user(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_admin_by_id(repository, admin_id):
        """Gets an admin from the database by their ID."""
        return repository.get_admin_by_id(admin_id=admin_id)

    @staticmethod
    @repository_method_wrapper
    def get_all_admins(repository):
        """Gets all admins from the database."""
        return repository.get_all_admins()

    @staticmethod
    @repository_method_wrapper
    def delete_admin_by_id(repository, admin_id: str):
        """Deletes an admin from the database by their ID."""
        return repository.delete_admin_by_id(admin_id=admin_id)

    @staticmethod
    @repository_method_wrapper
    def get_admin_by_email(repository, email: EmailStr):
        """Gets a user from the database by their email."""
        return repository.read_admin_by_email(email=email)
