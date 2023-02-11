from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:
    """A repository class for User models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the UserRepository class."""
        self.db = db

    def create_user(self, name, email, password):
        """Creates a new user in the system."""
        try:
            user = User(name=name, email=email, password=password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_superuser(self, name, email, password):
        """Creates a new superuser in the system."""
        try:
            user = User(name=name, email=email, password=password, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_admin(self, name, email, password):
        """Creates a new admin in the system."""
        try:
            user = User(name=name, email=email, password=password, is_admin=True)
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
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

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

    def update_user_is_active(self, user_id: str, is_active: bool):
        """Updates activity status of a user."""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def read_user_by_email(self, email: str):
        """Gets a user from the database by their email."""
        user = self.db.query(User).filter(User.email == email).first()
        return user
