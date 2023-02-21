import hashlib

from pydantic import EmailStr

from app.db.database import SessionLocal
from app.users.enums import UserStatus
from app.users.repository import CustomerRepository


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = CustomerRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class CustomerServices:
    """A service class for performing CRUD operations on Customer models."""

    @staticmethod
    @repository_method_wrapper
    def create_customer(repository, username: str, email: str, password: str):
        """Creates a new customer in the system."""
        hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        return repository.create_artist(username=username, email=email, password=hashed_password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return hashed_password == hashlib.sha256(bytes(plain_password, "utf-8")).hexdigest()

    @staticmethod
    @repository_method_wrapper
    def check_password(repository, customer_id: str, password: str):
        """Returns if the password is correct for the user_id."""
        user = repository.get_customer_by_id(customer_id=customer_id)
        if not user:
            return False
        hashed_password = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        return hashed_password == user.hashed_password

    @staticmethod
    @repository_method_wrapper
    def get_customer_by_id(repository, customer_id: str):
        """Gets a customer from the database by their ID."""
        return repository.get_customer_by_id(customer_id)

    @staticmethod
    @repository_method_wrapper
    def get_customer_by_username(repository, customer_username: str):
        """Gets a customer from the database by their username."""
        return repository.get_customer_by_username(customer_username)

    @staticmethod
    @repository_method_wrapper
    def get_customer_by_username_or_id_or_email(repository, identifier: str):
        """Gets a customer from the database by their username, ID, or email.."""
        return repository.get_customer_by_username_or_id_or_email(identifier)

    @staticmethod
    @repository_method_wrapper
    def get_all_customers(repository):
        """Gets all customers from the database."""
        return repository.get_all_customers()

    @staticmethod
    @repository_method_wrapper
    def delete_customer_by_id(repository, customer_id: str):
        """Deletes a customer from the database by their ID."""
        return repository.delete_customer_by_id(customer_id)

    @staticmethod
    @repository_method_wrapper
    def update_customer_status(repository, user_id: str, status: UserStatus):
        """Updates activity status of a customer."""
        return repository.update_customer_status(user_id, status)

    @staticmethod
    @repository_method_wrapper
    def get_customer_by_email(repository, email: str):
        """Gets a customer from the database by their email."""
        return repository.read_customer_by_email(email)

    @staticmethod
    @repository_method_wrapper
    def update_customer_email(repository, customer_id: str, email: str):
        """Updates a customer's email in the database."""
        return repository.update_customer_email(customer_id, email)
