from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.services import AdminServices


class AdminController:
    @staticmethod
    def create_admin(username: str, email: EmailStr, password: str):
        try:
            admin = AdminServices.create_admin(username=username, email=email, password=password)
            return admin
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail=f"Admin with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_admin_from_existing_user(user_id: str):
        try:
            admin = AdminServices.create_admin_from_existing_user(user_id=user_id)
            return admin
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Admin with provided ID {user_id} does not exist"
            )

    @staticmethod
    def get_superuser_by_id(admin_id: str):
        admin = AdminServices.get_admin_by_id(admin_id)
        if admin:
            return admin
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Admin with provided id {admin_id} does not exist",
            )

    @staticmethod
    def get_all_admins():
        admins = AdminServices.get_all_admins()
        return admins

    @staticmethod
    def delete_admin_by_id(admin_id: str):
        try:
            AdminServices.delete_admin_by_id(admin_id)
            return {"message": f"Admin with provided id {admin_id} was successfully deleted from the database."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
