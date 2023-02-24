"""Module for customer repository."""
from typing import Optional
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.enums import UserStatus
from app.users.models import Customer


class CustomerRepository:
    """A repository class for Customer models."""

    def __init__(self, db: Session):
        """Initializes a new instance of the CustomerRepository class."""
        self.db = db

    def create_customer(self, username, email, password):
        """Creates a new customer in the system."""
        try:
            customer = Customer(
                username=username,
                email=email,
                password=password
            )
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

    def get_customer_by_username(self, username: str):
        """Gets a customer from the database by their username."""
        try:
            customer = self.db.query(Customer).filter(Customer.username == username).first()
            return customer
        except Exception as e:
            raise e

    def get_customer_by_username_or_id_or_email(self, identifier: str) -> Optional[Customer]:
        """Gets a customer from the database by their username, ID, or email."""
        try:
            customer = self.db.query(Customer).filter((Customer.username == identifier) |
                                                      (Customer.id == identifier) |
                                                      (Customer.email == identifier)).first()
            return customer
        except Exception as e:
            raise e

    def get_all_customers(self):
        """Gets all customers from the database."""
        customers = self.db.query(Customer).all()
        return customers

    def delete_customer_by_id(self, customer_id: str):
        """Deletes a customer from the database by their ID."""
        try:
            customer = (
                self.db.query(Customer).filter(Customer.id == customer_id).first()
            )
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_customer_status(self, user_id: str, status: UserStatus):
        """Updates activity status of a customer."""
        try:
            customer = self.db.query(Customer).filter(Customer.id == user_id).first()
            customer.status = status
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            raise e

    def read_customer_by_email(self, email: str):
        """Gets a customer from the database by their email."""
        user = self.db.query(Customer).filter(Customer.email == email).first()
        return user

    def update_customer_email(self, customer_id: str, email: EmailStr) -> Customer:
        """Updates a customer's email in the database."""
        try:
            customer = self.get_customer_by_id(customer_id)
            customer.email = email
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            self.db.rollback()
            raise e
