import hashlib
from app.config import settings
from app.db.database import SessionLocal
from app.users.repository import SuperUserRepository
from app.users.schemas import SuperUserCreate


class SuperUserServices:
    @staticmethod
    def create_superuser(superuser: SuperUserCreate):
        with SessionLocal() as db:
            try:
                superuser_repository = SuperUserRepository(db)
                return superuser_repository.create_superuser(superuser)
            except Exception as e:
                raise e
