from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.services import CustomerServices
from app.users.models import UserStatus


class CustomerController:
    @staticmethod
    def create_customer(username: str, email: EmailStr, password: str):
        try:
            customer = CustomerServices.create_customer(username, email, password)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists")

    @staticmethod
    def get_customer_by_id(customer_id: str):
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return customer
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Customer with provided id {customer_id} does not exist",
            )

    @staticmethod
    def get_all_customers():
        customers = CustomerServices.get_all_customers()
        return customers

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        deleted = CustomerServices.get_customer_by_id(customer_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        CustomerServices.delete_customer_by_id(customer_id)
        return {"detail": "Customer deleted successfully"}

    @staticmethod
    def update_customer_status(user_id: str, status: UserStatus):
        customer = CustomerServices.get_customer_by_id(user_id)
        if not customer:
            raise HTTPException(status_code=404, detail="User not found")
        CustomerServices.update_customer_status(user_id, status)
        return {"detail": "Customer status updated successfully"}

    @staticmethod
    def read_customer_by_email(email: str):
        customer = CustomerServices.read_customer_by_email(email)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer
