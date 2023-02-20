from pydantic import UUID4, BaseModel, EmailStr
from typing import Optional
from app.users.enums import UserStatus, UserRole


class AdminBase(BaseModel):
    """A schema representing an Admin stored in the database"""
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.ADMIN


class AdminCreate(AdminBase):
    """A schema representing an Admin creation request"""
    name: str
    email: EmailStr
    password: str


class Admin(AdminBase):
    """A schema representing an Admin"""
    id: UUID4

    class Config:
        orm_mode = True
