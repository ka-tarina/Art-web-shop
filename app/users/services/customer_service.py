from app.db.database import SessionLocal
from app.users.enums import UserStatus
from app.users.repository import CustomerRepository


def repository_method_wrapper(func):
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
    def create_customer(repository, name: str, email: str, password: str):
        """Creates a new customer in the system."""
        return repository.create_artist(name, email, password, )

    @staticmethod
    @repository_method_wrapper
    def get_customer_by_id(repository, customer_id: str):
        """Gets a customer from the database by their ID."""
        return repository.get_customer_by_id(customer_id)

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
    def read_customer_by_email(repository, email: str):
        """Gets a customer from the database by their email."""
        return repository.read_customer_by_email(email)
