from pydantic import BaseModel
from typing import Optional
from app.users.models import UserStatus, UserRole


class Admin(BaseModel):
    """A schema representing an Admin stored in the database"""
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.ADMIN

    # from typing import List
    # from pydantic import BaseModel
    # from user import UserStatus
    #
    # class AdminCreate(BaseModel):
    #     """A schema representing an Admin creation request"""
    #     name: str
    #     email: str
    #     password: str
    #     status: UserStatus
    #
    # class AdminUpdate(BaseModel):
    #     """A schema representing an Admin update request"""
    #     name: str = None
    #     email: str = None
    #     password: str = None
    #     status: UserStatus = None
    #
    # class AdminInDB(AdminCreate):
    #     """A schema representing an Admin stored in the database"""
    #     id: str
    #
    #     class Config:
    #         orm_mode = True
    #
    # class Admin(AdminInDB):
    #     """A schema representing an Admin returned in responses"""
    #     artists: List[str] = []
