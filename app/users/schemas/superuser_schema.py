from typing import Optional
from pydantic import BaseModel, EmailStr
from app.users.models import UserRole, UserStatus


class SuperUser(BaseModel):
    """A schema representing a Superuser stored in the database"""
    id: str
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.SUPERUSER
    access_level: int

    class Config:
        orm_mode = True


class SuperUserIn(BaseModel):
    """A schema representing a Superuser creation request"""
    name: str
    email: EmailStr
    password: str
