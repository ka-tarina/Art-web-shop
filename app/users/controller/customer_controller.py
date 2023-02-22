from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.services import CustomerServices, UserAuthHandlerServices
from app.users.enums import UserStatus, UserRole


class CustomerController:
    @staticmethod
    def create_customer(username: str, email: EmailStr, password: str):
        """Creates a new customer in the system."""
        try:
            customer = CustomerServices.create_customer(username, email, password)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists")

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return CustomerServices.verify_password(plain_password, hashed_password)

    @staticmethod
    def check_password(customer_id: str, password: str):
        """Returns if the password is correct for the customer_id."""
        result = CustomerServices.check_password(customer_id=customer_id, password=password)
        if not result:
            raise HTTPException(status_code=400, detail="Invalid password")
        return result

    @staticmethod
    def login_customer(email, password):
        try:
            customer = CustomerServices.get_customer_by_email(email)
            if not customer:
                raise HTTPException(status_code=400, detail="Invalid email or password")
            if not CustomerServices.verify_password(password, customer.password):
                raise HTTPException(status_code=400, detail="Invalid email or password")
            return UserAuthHandlerServices.signJWT(customer.id, UserRole.CUSTOMER)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_id(customer_id: str):
        """Gets a customer from the database by their ID."""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return customer
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Customer with provided id {customer_id} does not exist",
            )

    @staticmethod
    def get_customer_by_username(customer_username: str):
        """Gets a customer from the database by their username."""
        customer = CustomerServices.get_customer_by_username(customer_username)
        if customer:
            return customer
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Customer with provided username {customer_username} does not exist",
            )

    @staticmethod
    def get_customer_by_identifier(identifier: str):
        """Gets a customer from the database by their username, ID, or email."""
        customer = CustomerServices.get_customer_by_username_or_id_or_email(identifier)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

    @staticmethod
    def get_all_customers():
        """Gets all customers from the database."""
        customers = CustomerServices.get_all_customers()
        return customers

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        """Deletes a customer from the database by their ID."""
        deleted = CustomerServices.get_customer_by_id(customer_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        CustomerServices.delete_customer_by_id(customer_id)
        return {"detail": "Customer deleted successfully"}

    @staticmethod
    def update_customer_status(user_id: str, status: UserStatus):
        """Updates activity status of a customer."""
        customer = CustomerServices.get_customer_by_id(user_id)
        if not customer:
            raise HTTPException(status_code=404, detail="User not found")
        CustomerServices.update_customer_status(user_id, status)
        return {"detail": "Customer status updated successfully"}

    @staticmethod
    def get_customer_by_email(email: str):
        """Gets a customer from the database by their email."""
        customer = CustomerServices.get_customer_by_email(email)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

    @staticmethod
    def update_customer_email(customer_id: str, email: str):
        """Updates a customer's email in the database."""
        try:
            result = CustomerServices.update_customer_email(customer_id, email)
            if not result:
                raise HTTPException(status_code=404, detail="Customer not found")
            return result
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Email already exists")
