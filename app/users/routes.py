from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.controller import CustomerController, ArtistController, AdminController, FollowController
from app.users.controller.user_auth_controller import JWTBearer
# from app.users.controller import SuperUserController
# from app.users.controller.user_auth_controller import JWTBearer
from app.users.controller.user_controller import UserController
from app.users.schemas import *
from app.users.services import SuperUserServices, ArtistServices

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

customer_router = APIRouter(tags=["customers"], prefix="/api/customers")


@customer_router.post("create-customer")
async def create_customer(name: str, email: EmailStr, password: str):
    customer = CustomerController.create_customer(name, email, password, )
    return customer


@customer_router.get("/get-all-customers")
async def get_all_customers():
    customers = CustomerController.get_all_customers()
    return customers


@customer_router.delete("/delete-customer-by-id/{customer_id}")
async def delete_customer_by_id(customer_id: str):
    response = CustomerController.delete_customer_by_id(customer_id)
    return response


@customer_router.put("/update-customer-status/{customer_id}")
async def update_customer_status(user_id: str, status: UserStatus):
    response = CustomerController.update_customer_status(user_id, status)
    return response


@customer_router.get("/read-customer-by-email/{email}")
async def read_customer_by_email(email: str):
    customer = CustomerController.read_customer_by_email(email)
    return customer

#  get customer by id missing

superuser_router = APIRouter(tags=["superusers"], prefix="/api/superusers")


@superuser_router.post("/create-superuser")
def create_superuser(username: str, email: EmailStr, password: str):
    try:
        superuser = SuperUserServices.create_superuser(username=username, email=email, password=password)
        return superuser
    except IntegrityError:
        raise HTTPException(
                status_code=400,
                detail=f"Superuser with provided email - {email} already exists.",
                )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@superuser_router.post("/create-from-existing-user")
def create_superuser_from_existing_user(user_id: str):
    try:
        superuser = SuperUserServices.create_superuser_from_existing_user(user_id=user_id)
        return superuser
    except Exception:
        raise HTTPException(
                status_code=400,
                detail=f"User with provided ID {user_id} does not exist"
                )


@superuser_router.get("/get-superuser-by-id/{superuser_id}")
def get_superuser_by_id(superuser_id: str):
    superuser = SuperUserServices.get_superuser_by_id(superuser_id)
    if superuser:
        return superuser
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Superuser with provided id {superuser_id} does not exist",
            )


@superuser_router.get("/get-all-superusers")
def get_all_superusers():
    superusers = SuperUserServices.get_all_superusers()
    return superusers


@superuser_router.delete("/delete-superuser-by-id/{superuser_id}")
def delete_superuser_by_id(superuser_id: str):
    try:
        deleted = SuperUserServices.get_superuser_by_id(superuser_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        SuperUserServices.delete_superuser_by_id(superuser_id)
        return {"detail": "Superuser deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


artist_router = APIRouter(tags=["artists"], prefix="/api/artists")


@artist_router.post("/create-artist")
async def create_artist(email: EmailStr, username: str, password: str):
    artist = ArtistController.create_artist(email, username, password)
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


@admin_router.post("create-admin")
async def create_admin(username: str, email: EmailStr, password: str):
    return AdminController.create_admin(username, email, password)


@admin_router.post("/create-admin-from-existing-user/{user_id}")
async def create_admin_from_existing_user(user_id: str):
    return AdminController.create_admin_from_existing_user(user_id)


@admin_router.get("/get-admin-by-id/{admin_id}")
async def get_admin_by_id(admin_id: str):
    return AdminController.get_admin_by_id(admin_id)


@admin_router.get("get-all-admins")
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
