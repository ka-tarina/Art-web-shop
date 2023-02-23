"""Model for admin controller"""
from fastapi import HTTPException
from pydantic import EmailStr
from app.users.exceptions import UserNotFoundError
from app.users.services import AdminServices


class AdminController:
    @staticmethod
    def create_admin(username: str, email: EmailStr, password: str):
        """Creates a new admin in the system."""
        try:
            user_exist = AdminServices.get_admin_by_email(email=email)
            if user_exist:
                raise HTTPException(
                    status_code=400,
                    detail=f"User with provided email - {email} already exists.",
                )
            return AdminServices.create_admin(
                username=username, email=email, password=password
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_admin_from_existing_user(user_id: str):
        """Creates a new admin in the system from existing user."""
        try:
            admin = AdminServices.create_admin_from_existing_user(user_id=user_id)
            return admin
        except UserNotFoundError:
            raise HTTPException(
                status_code=400,
                detail=f"Admin with provided ID {user_id} does not exist",
            )

    @staticmethod
    def get_admin_by_id(admin_id: str):
        """Gets an admin from the database by their ID."""
        try:
            admin = AdminServices.get_admin_by_id(admin_id)
            return admin
        except UserNotFoundError:
            raise HTTPException(
                status_code=400,
                detail=f"Admin with provided id {admin_id} does not exist",
            )

    @staticmethod
    def get_all_admins():
        """Gets all admins from the database."""
        admins = AdminServices.get_all_admins()
        return admins

    @staticmethod
    def delete_admin_by_id(admin_id: str):
        """Deletes an admin from the database by their ID."""
        try:
            deleted = AdminServices.get_admin_by_id(admin_id)
            if not deleted:
                raise UserNotFoundError(code=404, message="User not found")
            AdminServices.delete_admin_by_id(admin_id)
            return {"detail": f"Admin deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
