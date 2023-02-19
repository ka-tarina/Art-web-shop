from pydantic import UUID4, BaseModel, EmailStr
from app.users.models import UserRole, UserStatus


class CustomerSchemaBase(BaseModel):
    """Base model for representing a Customer."""
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.CUSTOMER


class CustomerSchemaCreate(CustomerSchemaBase):
    """A schema representing a Customer creation request"""
    name: str
    email: EmailStr
    password: str
    role: UserRole
    status: UserStatus


class CustomerSchema(CustomerSchemaBase):
    """A schema representing a Customer"""
    id: UUID4

    class Config:
        orm_mode = True
