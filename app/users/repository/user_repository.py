"""Module for user repository."""
import hashlib
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User
from app.users.enums import UserRole, UserStatus


class UserRepository:
    """A repository class for User models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the UserRepository class."""
        self.db = db

    def create_user(self, username, email, password):
        """Creates a new user in the system."""
        try:
            user = User(
                username=username,
                email=email,
                password=password,
                role=UserRole.CUSTOMER,
                status=UserStatus.ACTIVE)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_user_by_id(self, user_id: str):
        """Gets a user from the database by their ID."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            raise e

    def get_user_by_username(self, username: str):
        """Gets a user from the database by their username."""
        try:
            user = self.db.query(User).filter(User.username == username).first()
            return user
        except Exception as e:
            raise e

    def get_user_by_username_or_id(self, username_or_id: str):
        """Gets a user from the database by their username or their ID."""
        try:
            user = self.db.query(User).filter((User.username == username_or_id) |
                                              (User.id == username_or_id)).first()
            return user
        except Exception as e:
            raise e

    def read_user_by_email(self, email: EmailStr):
        """Gets a user from the database by their email."""
        try:
            user = self.db.query(User).filter(User.email == email).first()
            return user
        except Exception as e:
            raise e

    def get_user_by_username_or_id_or_email(self, username_id_email: str):
        """Gets a user from the database by either their username, ID or email."""
        try:
            user = self.db.query(User).filter((User.username == username_id_email) |
                                              (User.id == username_id_email) |
                                              (User.email == username_id_email)).first()
            return user
        except Exception as e:
            raise e

    def update_user_email(self, email: EmailStr, new_email: EmailStr):
        """Updates the email of the user."""
        try:
            user = self.read_user_by_email(email)
            user.new_email = new_email
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def check_password(self, user_id: str, password: str):
        """Returns if the password is correct for the user_id."""
        user = self.get_user_by_id(user_id=user_id)
        if not user:
            return False
        hashed_password = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        return hashed_password == user.hashed_password

    def update_user_password(self, email: EmailStr, new_password: str):
        """Updates the password of the user."""
        try:
            user = self.read_user_by_email(email)
            user.password = new_password
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_status(self, user_id: str, status: UserStatus):
        """Updates the status of the user."""
        try:
            user = self.get_user_by_id(user_id)
            user.status = status
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_role(self, user_id: str, role: UserRole):
        """Updates the role of the user."""
        try:
            user = self.get_user_by_id(user_id)
            user.role = role
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def get_all_users(self):
        """Gets all users from the database."""
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id: str):
        """Deletes a user from the database by their ID."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e
