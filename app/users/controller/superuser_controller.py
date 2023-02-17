from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.users.schemas import SuperUserCreate
from app.users.services import SuperUserServices


class SuperUserController:
    @staticmethod
    def create_superuser(superuser: SuperUserCreate):
        try:
            user = SuperUserServices.create_superuser(superuser=superuser)
            return user
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {superuser.email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
