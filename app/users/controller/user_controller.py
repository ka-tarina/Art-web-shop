from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.users.exceptions import UserInvalidPassword
from app.users.services import UserServices, signJWT


class UserController:
    @staticmethod
    def create_user(name, email, password):
        try:
            user = UserServices.create_user(name, email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_superuser(name, email, password):
        try:
            user = UserServices.create_superuser(name, email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserServices.login_user(email, password)
            if user.is_superuser:
                return signJWT(user.id, "super_user")
            return signJWT(user.id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"user with provided id {user_id} does not exist",
            )

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id}, is deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            UserServices.update_user_is_active(user_id, is_active)
            return {"message": f"Activity status of user with provided id, {user_id} has been updated"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
