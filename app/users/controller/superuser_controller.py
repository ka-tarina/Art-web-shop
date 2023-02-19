from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.services import SuperUserServices


class SuperUserController:
    @staticmethod
    def create_superuser(username: str, email: EmailStr, password: str):
        try:
            superuser = SuperUserServices.create_superuser(username=username, email=email, password=password)
            return superuser
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail=f"Superuser with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_superuser_from_existing_user(user_id: str):
        try:
            superuser = SuperUserServices.create_superuser_from_existing_user(user_id=user_id)
            return superuser
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided ID {user_id} does not exist"
            )

    @staticmethod
    def get_superuser_by_id(superuser_id: str):
        superuser = SuperUserServices.get_superuser_by_id(superuser_id)
        if superuser:
            return superuser
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Superuser with provided id {superuser_id} does not exist",
            )

    @staticmethod
    def get_all_superusers():
        superusers = SuperUserServices.get_all_superusers()
        return superusers

    @staticmethod
    def delete_superuser_by_id(superuser_id: str):
        try:
            deleted = SuperUserServices.get_superuser_by_id(superuser_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="User not found")
            SuperUserServices.delete_superuser_by_id(superuser_id)
            return {"detail": "Superuser deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
