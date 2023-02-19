from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr
from app.users.models import UserRole, UserStatus


class SuperUserBase(BaseModel):
    """Base model for representing a Superuser."""
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.SUPERUSER


class SuperUserCreate(SuperUserBase):
    """A schema representing a Superuser creation request"""
    name: str
    email: EmailStr
    password: str
    role: UserRole
    status: UserStatus


class SuperUser(SuperUserBase):
    """A schema representing a Superuser"""
    id: UUID4

    class Config:
        orm_mode = True
