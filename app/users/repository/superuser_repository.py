from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.schemas import SuperUser, SuperUserCreate, UserStatus, UserRole


class SuperUserRepository:
    """A repository class for User models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the UserRepository class."""
        self.db = db

    def create_superuser(self, superuser: SuperUserCreate) -> SuperUser:
        """Creates a new superuser in the system."""
        try:
            user = SuperUser(
                name=superuser.name,
                email=superuser.email,
                password=superuser.password,
                role=superuser.role,
                status=superuser.status)
            self.db.add(superuser)
            self.db.commit()
            self.db.refresh(superuser)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e
