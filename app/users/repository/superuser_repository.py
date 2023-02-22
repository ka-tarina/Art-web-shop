"""Module for superuser repository."""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.enums import UserRole
from app.users.models import SuperUser
from app.users.repository import UserRepository


class SuperUserRepository(UserRepository):
    """A repository class for Superuser models."""

    def __init__(self, db: Session):
        """Initializes a new instance of the SuperuserRepository class."""
        super().__init__(db)

    def create_superuser(self, username, email, password):
        """Creates a new superuser in the system."""
        try:
            superuser = SuperUser(username=username, email=email, password=password)
            self.db.add(superuser)
            self.db.commit()
            self.db.refresh(superuser)
            return superuser
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_superuser_from_existing_user(self, user_id: str):
        """Creates a superuser from an existing user."""
        try:
            user = self.get_user_by_id(user_id=user_id)
            superuser = SuperUser(username=user.username, email=user.email, password=user.password)
            self.db.add(superuser)
            self.db.commit()
            self.db.refresh(superuser)
            return superuser
        except Exception as e:
            raise e

    def get_superuser_by_id(self, superuser_id: str):
        """Gets a superuser from the database by their ID."""
        user = self.get_user_by_id(superuser_id)
        if user.role == UserRole.SUPERUSER:
            return SuperUser.from_orm(user)

    def get_all_superusers(self):
        """Gets all superusers from the database."""
        superusers = self.db.query(SuperUser).all()
        return superusers

    def delete_superuser_by_id(self, superuser_id: str):
        """Deletes a superuser from the database by their ID."""
        try:
            superuser = self.get_superuser_by_id(superuser_id)
            if superuser:
                self.db.delete(superuser)
                self.db.commit()
            return True
        except Exception as e:
            raise e
