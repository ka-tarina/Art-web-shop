from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.enums import UserRole
from app.users.models import Admin
from app.users.repository import UserRepository


class AdminRepository(UserRepository):
    """A repository class for Admin models."""

    def __init__(self, db: Session):
        """Initializes a new instance of the AdminRepository class."""
        super().__init__(db)

    def create_admin(self, username, email, password):
        """Creates a new admin in the system."""
        try:
            admin = Admin(username=username, email=email, password=password)
            self.db.add(admin)
            self.db.commit()
            self.db.refresh(admin)
            return admin
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    # def create_admin_from_existing_user(self, user_id: str):
    #     """Creates an admin from an existing user."""
    #     try:
    #         admin = self.update_user_role(user_id=user_id, role=UserRole.ADMIN)
    #         return admin
    #     except Exception as e:
    #         raise e

    def get_admin_by_id(self, admin_id: str):
        """Gets a superuser from the database by their ID."""
        admin = self.db.query(Admin).get(admin_id)
        if admin is None:
            raise Exception(f"Artist with ID {admin_id} not found")
        return admin

    def get_all_admins(self):
        """Gets all superusers from the database."""
        admins = self.db.query(Admin).all()
        return admins

    def delete_admin_by_id(self, admin_id: str):
        """Deletes a superuser from the database by their ID."""
        try:
            admin = self.get_admin_by_id(admin_id)
            if admin:
                self.db.delete(admin)
                self.db.commit()
            return True
        except Exception as e:
            raise e
