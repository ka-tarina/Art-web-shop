from pydantic import UUID4
from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Customer, UserStatus


class UserRepository:
    """A repository class for Customer models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the Customer class."""
        self.db = db

    def create_customer(self, name, email, password):
        """Creates a new customer in the system."""
        try:
            customer = Customer(name=name, email=email, password=password, status=UserStatus.ACTIVE)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_customer_by_id(self, customer_id: str):
        """Gets a customer from the database by their ID."""
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        return customer

    def get_all_customers(self):
        """Gets all users from the database."""
        users = self.db.query(Customer).all()
        return users

    def delete_customer_by_id(self, user_id: str):
        """Deletes a user from the database by their ID."""
        try:
            customer = self.db.query(Customer).filter(Customer.id == user_id).first()
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_customer_status(self, user_id: str, status: bool):
        """Updates activity status of a user."""
        try:
            customer = self.db.query(Customer).filter(Customer.id == user_id).first()
            user.is_active = is_active
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def read_user_by_email(self, email: str):
        """Gets a user from the database by their email."""
        user = self.db.query(User).filter(User.email == email).first()
        return user
