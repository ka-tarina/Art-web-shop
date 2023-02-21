from pydantic import UUID4, BaseModel, EmailStr
from app.users.enums import UserRole, UserStatus


class CustomerSchema(BaseModel):
    """A schema representing a Customer."""
    id: UUID4
    name: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.CUSTOMER

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    """A schema representing a Customer creation request"""
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
