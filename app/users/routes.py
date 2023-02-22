from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from app.users.controller import (
    AdminController,
    ArtistController,
    CustomerController,
    FollowController,
    SuperUserController,
)
from app.users.controller.user_auth_controller import JWTBearer
# from app.users.controller import SuperUserController
# from app.users.controller.user_auth_controller import JWTBearer
from app.users.controller.user_controller import UserController
from app.users.models import User
from app.users.schemas import *
from app.users.schemas.user_schema import LoginSchema
from app.users.services import ArtistServices, SuperUserServices


user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/login")
def login_user(user: LoginSchema):
    return UserController.login_user(user.email, user.password)


@user_router.get("/get-user-by-id/{user_id}",
                 response_model=UserSchema,
                 dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users",
                 response_model=list[UserSchema],
                 dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


customer_router = APIRouter(tags=["customers"], prefix="/api/customers")


@customer_router.post("/create-customer", response_model=CustomerSchema)
async def create_customer(customer: CustomerSchemaIn):
    customer = CustomerController.create_customer(customer.username, customer.email, customer.password)
    return customer


@customer_router.get("/get-all-customers",
                     response_model=list[CustomerSchema],
                     dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
async def get_all_customers():
    customers = CustomerController.get_all_customers()
    return customers


@customer_router.get("/get-customer-by-id/{customer_id}", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    customer = CustomerController.get_customer_by_id(customer_id=customer_id)
    return customer


@customer_router.get("/get-customer-by-username/{customer_username}", response_model=CustomerSchema)
def get_customer_by_username(customer_username: str):
    customer = CustomerController.get_customer_by_username(customer_username=customer_username)
    return customer


@customer_router.get("/get-customer-by-username/{customer_username}", response_model=CustomerSchema)
def get_customer_by_identifier(identifier: str):
    customer = CustomerController.get_customer_by_identifier(identifier=identifier)
    return customer


@customer_router.delete("/delete-customer-by-id/{customer_id}",
                        dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
async def delete_customer_by_id(customer_id: str):
    response = CustomerController.delete_customer_by_id(customer_id)
    return response


@customer_router.put("/update-customer-status/{customer_id}",
                     response_model=CustomerSchema,
                     dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
async def update_customer_status(customer: UpdateCustomerSchema):
    response = CustomerController.update_customer_status(customer.customer_id, customer.status)
    return response


@customer_router.get("/read-customer-by-email/{email}", response_model=CustomerSchemaOut)
async def read_customer_by_email(email: str):
    customer = CustomerController.get_customer_by_email(email)
    return customer


@customer_router.put("/update-customer-email/{email}",
                     response_model=CustomerSchema,
                     dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
async def update_customer_email(customer: UpdateCustomerSchema):
    response = CustomerController.update_customer_email(customer.customer_id, customer.email)
    return response


superuser_router = APIRouter(tags=["superusers"], prefix="/api/superusers")


@superuser_router.post("/create-superuser")
async def create_superuser(username: str, email: EmailStr, password: str):
    superuser = SuperUserController.create_superuser(
        username=username, email=email, password=password
    )
    return superuser


# @superuser_router.post("/create-from-existing-user")
# def create_superuser_from_existing_user(user_id: str):
#     superuser = SuperUserController.create_superuser_from_existing_user(user_id=user_id)
#     return superuser


@superuser_router.get("/get-superuser-by-id/{superuser_id}")
async def get_superuser_by_id(superuser_id: str):
    superuser = SuperUserController.get_superuser_by_id(superuser_id)
    return superuser


@superuser_router.get("/get-all-superusers")
async def get_all_superusers():
    superusers = SuperUserController.get_all_superusers()
    return superusers


@superuser_router.delete("/delete-superuser-by-id/{superuser_id}")
async def delete_superuser_by_id(superuser_id: str):
    SuperUserController.delete_superuser_by_id(superuser_id=superuser_id)


artist_router = APIRouter(tags=["artists"], prefix="/api/artists")


@artist_router.post("/create-artist")
async def create_artist(username: str, email: EmailStr, password: str, bio, website):
    artist = ArtistController.create_artist(username, email, password, bio, website)
    return artist


@artist_router.get("/get-artist-by-id/{artist_id}")
async def get_artist_by_id(artist_id: str):
    artist = ArtistController.get_artist_by_id(artist_id)
    return artist


@artist_router.get("/get-artist-by-username/{username}")
async def get_artist_by_username(username: str):
    artist = ArtistController.get_artist_by_username(username)
    return artist


@artist_router.get("/get-all-artists")
async def get_all_artists():
    artists = ArtistController.get_all_artists()
    return artists


@artist_router.put("/update-artist-bio/{artist_id}")
async def update_artist_bio(artist_id: str, bio: str):
    ArtistController.update_artist_bio(artist_id, bio)
    return {"detail": "Artist bio updated successfully"}


@artist_router.put("/update-artist-website/{artist_id}")
async def update_artist_website(artist_id: str, website: str):
    ArtistController.update_artist_website(artist_id, website)
    return {"detail": "Artist website updated successfully"}


@artist_router.delete("/delete-artist-by-id/{artist_id}")
async def delete_artist_by_id(artist_id: str):
    ArtistController.delete_artist_by_id(artist_id)
    return {"detail": "Artist deleted successfully"}


admin_router = APIRouter(tags=["admins"], prefix="/api/admins")


@admin_router.post("/create-admin", response_model=AdminSchema)
async def create_admin(admin: AdminSchemaIn):
    return AdminController.create_admin(admin.username, admin.email, admin.password)


# @admin_router.post(
#     "/create-admin-from-existing-user/{user_id}", response_model=AdminSchema
# )
# async def create_admin_from_existing_user(user_id: str):
#     return AdminController.create_admin_from_existing_user(user_id)


@admin_router.get("/get-admin-by-id/{admin_id}", response_model=AdminSchema)
async def get_admin_by_id(admin_id: str):
    return AdminController.get_admin_by_id(admin_id)


@admin_router.get("/get-all-admins", response_model=list[AdminSchema])
async def get_all_admins():
    return AdminController.get_all_admins()


@admin_router.delete("/delete-admin-by-id/{admin_id}")
async def delete_admin_by_id(admin_id: str):
    return AdminController.delete_admin_by_id(admin_id)


follow_router = APIRouter(tags=["follows"], prefix="/api/follows")


@follow_router.post("/follow-artist/{customer_id}/{artist_id}")
async def follow_artist(customer_id: str, artist_id: str):
    return FollowController.follow_artist(customer_id, artist_id)


@follow_router.post("/unfollow-artist/{customer_id}/{artist_id}")
async def unfollow_artist(customer_id: str, artist_id: str):
    return FollowController.unfollow_artist(customer_id, artist_id)


@follow_router.get("/get-following-artists/{customer_id}")
async def get_following_artists(customer_id: str):
    return FollowController.get_following_artists(customer_id)


@follow_router.get("/get-followers/{artist_id}")
async def get_followers(artist_id: str):
    return FollowController.get_followers(artist_id)
