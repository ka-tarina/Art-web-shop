"""Module for user controller"""
from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from app.users.exceptions import UserInvalidPassword
from app.users.enums import UserRole, UserStatus
from app.users.services import UserServices, signJWT


class UserController:
    """A controller class for User models."""
    @staticmethod
    def create_user(username, email, password):
        """Creates a new user in the system."""
        try:
            user = UserServices.create_user(username, email, password)
            return user
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        """Logs user in the system."""
        try:
            user = UserServices.login_user(email, password)
            if user.role == UserRole.SUPERUSER:
                return signJWT(user.id, UserRole.SUPERUSER)
            elif user.role == UserRole.ADMIN:
                return signJWT(user.id, UserRole.ADMIN)
            elif user.role == UserRole.ARTIST:
                return signJWT(user.id, UserRole.ARTIST)
            return signJWT(user.id, UserRole.CUSTOMER)
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def register_user(username: str, email: EmailStr, password: str):
        """Registers user in the system."""
        if UserServices.get_user_by_email(email):
            raise HTTPException(status_code=400, detail="Email already registered")
        elif UserServices.get_user_by_username(username):
            raise HTTPException(status_code=400, detail="Username already registered")
        UserServices.create_user(username, email, password)
        return {"detail": "User registered successfully"}

    @staticmethod
    def get_user_by_id(user_id: str):
        """Gets a user from the database by their ID."""
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided id {user_id} does not exist",
            )

    @staticmethod
    def get_user_by_username(username: str):
        """Gets a user from the database by their username."""
        user = UserServices.get_user_by_username(username)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided username {username} does not exist",
            )

    @staticmethod
    def get_user_by_username_or_id(username_or_id: str):
        """Gets a user from the database by their ID or username."""
        user = UserServices.get_user_by_username_or_id(username_or_id)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided identification {username_or_id} does not exist",
            )

    @staticmethod
    def get_user_by_email(email: EmailStr):
        """Gets a user from the database by their email."""
        user = UserServices.get_user_by_email(email)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email {email} does not exist",
            )

    @staticmethod
    def get_user_by_username_or_id_or_email(username_id_email: str):
        """Gets a user from the database by their ID, email or username."""
        user = UserServices.get_user_by_username_or_id_or_email(username_id_email)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided identification {username_id_email} does not exist",
            )

    @staticmethod
    def update_user_email(email: EmailStr, new_email: EmailStr):
        """Updates email of user."""
        user = UserServices.update_user_email(email=email, new_email=new_email)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email {email} does not exist",
            )

    @staticmethod
    def update_user_password(email: str, password: str, new_password: str):
        """Updates user password"""
        try:
            user = UserServices.update_user_password(
                email=email,
                password=password,
                new_password=new_password
            )
            return user
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email {email} does not exist"
            )

    @staticmethod
    def update_user_status(username_id_email: str, status: UserStatus):
        """Updates user status"""
        try:
            user = UserServices.update_user_status(username_id_email=username_id_email, status=status)
            return user
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided identification {username_id_email} does not exist"
            )

    @staticmethod
    def update_user_role(username_id_email: str, role: UserRole):
        """Updates user role"""
        try:
            user = UserServices.update_user_role(username_id_email=username_id_email, role=role)
            return user
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided identification {username_id_email} does not exist"
            )

    @staticmethod
    def get_all_users():
        """Gets all users from the database."""
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Deletes a user from the database by their ID."""
        try:
            deleted = UserServices.get_user_by_id(user_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="User not found")
            UserServices.delete_user_by_id(user_id)
            return {
                "detail": f"User with provided id {user_id} was successfully deleted from the database."
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
