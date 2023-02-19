from fastapi import APIRouter, Depends

from app.users.controller.user_auth_controller import JWTBearer
# from app.users.controller import SuperUserController
# from app.users.controller.user_auth_controller import JWTBearer
from app.users.controller.user_controller import UserController
from app.users.schemas import *

user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.name, user.email, user.password)


# @user_router.post("/add-new-super-user", response_model=SuperUser,) #dependencies=[Depends(JWTBearer("super_user"))])
# def create_superuser(superuser: SuperUserCreate):
#     return UserController.create_superuser(superuser=superuser)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer(UserRole.SUPERUSER))])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTBearer(UserRole.SUPERUSER))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


# @user_router.put("/update/is_active", response_model=UserSchema)
# def update_user(user_id: str, is_active: bool):
#     return UserController.update_user_is_active(user_id, is_active)

router = APIRouter()
@router.post("/customers")
async def create_customer(name: str, email: EmailStr, password: str):
    customer = CustomerController.create_artist(name, email, password, )
    return customer

@router.get("/customers")
async def get_all_customers():
    customers = CustomerController.get_all_customers()
    return customers

@router.delete("/customers/{customer_id}")
async def delete_customer_by_id(customer_id: str):
    response = CustomerController.delete_customer_by_id(customer_id)
    return response

@router.put("/customers/{user_id}")
async def update_customer_status(user_id: str, status: UserStatus):
    response = CustomerController.update_customer_status(user_id, status)
    return response

@router.get("/customers/{email}")
async def read_customer_by_email(email: str):
    customer = CustomerController.read_customer_by_email(email)
    return customer

#get customer by id missing