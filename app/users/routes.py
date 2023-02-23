"""
API for user management. It includes routes for user authentication,
creating, deleting and updating users, managing customers, and
managing superusers.
"""
from fastapi import APIRouter, Depends
from app.users.controller import (
    AdminController,
    ArtistController,
    CustomerController,
    FollowController,
    SuperUserController,
)
from app.users.controller.user_auth_controller import JWTBearer
from app.users.controller.user_controller import UserController
from app.users.schemas import *


user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/login")
def login_user(user: LoginSchema):
    """Logs in a user."""
    return UserController.login_user(user.email, user.password)


@user_router.get("/get-user-by-id/{user_id}",
                 response_model=UserSchema)
def get_user_by_id(user_id: str):
    """gets a user by ID, expects a user_id, only available for admin or superuser roles"""
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users",
                 response_model=list[UserSchema])
def get_all_users():
    """Gets all users, only available for admin or superuser roles"""
    return UserController.get_all_users()


@user_router.delete("/")#, dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
def delete_user_by_id(user_id: str):
    """Deletes a user by ID, expects a user_id, only available for superuser role"""
    return UserController.delete_user_by_id(user_id)


customer_router = APIRouter(tags=["customers"], prefix="/api/customers")


@customer_router.post("/create-customer", response_model=CustomerSchema)
async def create_customer(customer: CustomerSchemaIn):
    """Creates a new customer"""
    customer = CustomerController.create_customer(customer.username,
                                                  customer.email,
                                                  customer.password)
    return customer


@customer_router.get("/get-all-customers",
                     response_model=list[CustomerSchema])
async def get_all_customers():
    """Gets all customers, only available for admin or superuser roles"""
    customers = CustomerController.get_all_customers()
    return customers


@customer_router.get("/get-customer-by-id/{customer_id}", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    """Gets a customer by ID"""
    customer = CustomerController.get_customer_by_id(customer_id=customer_id)
    return customer


@customer_router.get("/get-customer-by-username", response_model=CustomerSchema)
def get_customer_by_username(customer_username: str):
    """Gets a customer by username"""
    customer = CustomerController.get_customer_by_username(customer_username=customer_username)
    return customer


@customer_router.get("/get-customer-by-identifier", response_model=CustomerSchema)
def get_customer_by_identifier(identifier: str):
    """Gets a customer by ID, username or email"""
    customer = CustomerController.get_customer_by_identifier(identifier=identifier)
    return customer


@customer_router.delete("/delete-customer-by-id/{customer_id}",
                        dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
async def delete_customer_by_id(customer_id: str):
    """Deletes a customer by ID, only available for superuser role"""
    response = CustomerController.delete_customer_by_id(customer_id)
    return response


@customer_router.put("/update-customer-status/{customer_id}",
                     response_model=CustomerSchema,
                     dependencies=[Depends(JWTBearer(roles=[UserRole.ADMIN, UserRole.SUPERUSER]))])
async def update_customer_status(customer: UpdateCustomerStatusSchema):
    """Updates a customer's status, only available for admin or superuser roles"""
    response = CustomerController.update_customer_status(customer.customer_id, customer.status)
    return response


@customer_router.get("/get-customer-by-email/{email}", response_model=CustomerSchemaOut)
async def get_customer_by_email(email: str):
    """Gets a customer by email"""
    customer = CustomerController.get_customer_by_email(email)
    return customer


@customer_router.put("/update-customer-email/{email}",
                     response_model=CustomerSchema)
async def update_customer_email(customer: UpdateCustomerEmailSchema):
    """Updates a customer's email, only available for admin or superuser roles"""
    response = CustomerController.update_customer_email(customer.customer_id, customer.email)
    return response


@customer_router.post("/follow-artist/{customer_id}/{artist_id}",
                      response_model=CustomerFollowedArtistSchema)
# ,
                      # dependencies=[Depends(JWTBearer(roles=[UserRole.CUSTOMER]))])
async def follow_artist(follow_id: FollowSchema):
    """Allows a customer to follow an artist, only available for customer role"""
    return FollowController.follow_artist(follow_id.customer_id, follow_id.artist_id)


@customer_router.post("/unfollow-artist/{customer_id}/{artist_id}",
                      response_model=CustomerFollowedArtistSchema)
    # ,
    #                   dependencies=[Depends(JWTBearer(roles=[UserRole.CUSTOMER]))])
async def unfollow_artist(unfollow_id: FollowSchema):
    """Allows a customer to unfollow an artist, only available for customer role"""
    return FollowController.unfollow_artist(unfollow_id.customer_id, unfollow_id.artist_id)


@customer_router.get("/get-following-artists/{customer_id}",
                     response_model=FollowingArtistsSchema)
async def get_following_artists(customer_id: str):
    """Gets the artists a customer is following"""
    return FollowController.get_following_artists(customer_id)


superuser_router = APIRouter(tags=["superusers"], prefix="/api/superusers")


@superuser_router.post("/create-superuser", response_model=SuperUserSchema)
async def create_superuser(superuser: SuperUserSchemaIn):
    """Creates a new superuser"""
    superuser = SuperUserController.create_superuser(
        superuser.username, superuser.email, superuser.password
    )
    return superuser


@superuser_router.get("/get-superuser-by-id/{superuser_id}",
                      response_model=SuperUserSchema)
async def get_superuser_by_id(superuser_id: str):
    """Gets a superuser by ID, only available for superuser role"""
    superuser = SuperUserController.get_superuser_by_id(superuser_id)
    return superuser


@superuser_router.get("/get-all-superusers",
                      response_model=list[SuperUserSchema])
async def get_all_superusers():
    """Gets all superusers, only available for superuser role"""
    superusers = SuperUserController.get_all_superusers()
    return superusers


@superuser_router.delete("/delete-superuser-by-id/{superuser_id}",
                         response_model=SuperUserSchema,
                         dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
async def delete_superuser_by_id(superuser_id: str):
    """Deletes a superuser by ID, only available for superuser role"""
    SuperUserController.delete_superuser_by_id(superuser_id=superuser_id)


artist_router = APIRouter(tags=["artists"], prefix="/api/artists")


@artist_router.post("/create-artist",
                    response_model=ArtistSchema)
async def create_artist(artist: ArtistSchemaIn):
    """Creates a new artist with the given username, email, password, bio, and website."""
    artist = ArtistController.create_artist(artist.username,
                                            artist.email,
                                            artist.password,
                                            artist.bio,
                                            artist.website)
    return artist


@artist_router.get("/get-artist-by-id/{artist_id}",
                   response_model=ArtistSchema)
async def get_artist_by_id(artist_id: str):
    """Gets the artist with the given artist ID."""
    artist = ArtistController.get_artist_by_id(artist_id)
    return artist


@artist_router.get("/get-artist-by-username/{username}",
                   response_model=ArtistSchemaOut)
async def get_artist_by_username(username: str):
    """Gets the artist with the given username"""
    artist = ArtistController.get_artist_by_username(username)
    return artist


@artist_router.get("/get-all-artists",
                   response_model=list[ArtistSchema])
async def get_all_artists():
    """Gets a list of all artists."""
    artists = ArtistController.get_all_artists()
    return artists


@artist_router.put("/update-artist-bio/{artist_id}",
                   response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer(roles=[UserRole.ARTIST, UserRole.ADMIN, UserRole.SUPERUSER]))])
async def update_artist_bio(artist: ArtistSchemaUpdate):
    """Updates the bio of the artist"""
    artist = ArtistController.update_artist_bio(artist.id, artist.bio)
    return artist


@artist_router.put("/update-artist-website/{artist_id}",
                   response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer(roles=[UserRole.ARTIST, UserRole.SUPERUSER, UserRole.ADMIN]))])
async def update_artist_website(artist: ArtistSchemaUpdate):
    """Updates the website of the artist"""
    artist = ArtistController.update_artist_website(artist.id, artist.bio)
    return artist


@artist_router.delete("/delete-artist-by-id/{artist_id}",
                      dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
async def delete_artist_by_id(artist_id: str):
    """Deletes artist with the given artist_id."""
    return ArtistController.delete_artist_by_id(artist_id)


@artist_router.get("/get-followers/{artist_id}",
                   response_model=FollowersSchema)
async def get_followers(artist_id: str):
    """Gets the followers of the artist."""
    return FollowController.get_followers(artist_id)


@artist_router.get("/top-artists-by-followers/{limit}",
                   response_model=TopFollowersSchema)
async def get_top_artists_by_followers(limit: int):
    """Gets the top artists by number of followers, limited to the given limit."""
    data = FollowController.get_artists_by_followers(limit)
    return data


admin_router = APIRouter(tags=["admins"], prefix="/api/admins")


@admin_router.post("/create-admin",
                   response_model=AdminSchema,
                   dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER, UserRole.ADMIN]))])
async def create_admin(admin: AdminSchemaIn):
    """Creates a new admin with the given username, email, and password."""
    return AdminController.create_admin(admin.username, admin.email, admin.password)


@admin_router.get("/get-admin-by-id/{admin_id}",
                  response_model=AdminSchema)
async def get_admin_by_id(admin_id: str):
    """Gets the admin with the given admin_id."""
    return AdminController.get_admin_by_id(admin_id)


@admin_router.get("/get-all-admins",
                  response_model=list[AdminSchema])
async def get_all_admins():
    """Gets a list of all admins."""
    return AdminController.get_all_admins()


@admin_router.delete("/delete-admin-by-id/{admin_id}",
                     dependencies=[Depends(JWTBearer(roles=[UserRole.SUPERUSER]))])
async def delete_admin_by_id(admin_id: str):
    """Deletes the admin with the given admin_id."""
    return AdminController.delete_admin_by_id(admin_id)
