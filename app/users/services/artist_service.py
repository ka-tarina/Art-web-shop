"""Module for artist service."""
import hashlib
from app.db.database import SessionLocal
from app.users.repository import ArtistRepository


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = ArtistRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class ArtistServices:
    """A service class for performing CRUD operations on Artist models."""

    @staticmethod
    @repository_method_wrapper
    def create_artist(repository,
                      username: str,
                      email: str,
                      password: str,
                      bio: str = "",
                      website: str = ""):
        """Creates a new artist in the system."""
        hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        return repository.create_artist(username=username,
                                        email=email,
                                        password=hashed_password,
                                        bio=bio,
                                        website=website)

    @staticmethod
    @repository_method_wrapper
    def get_artist_by_id(repository, artist_id: str):
        """Gets an artist from the database by their ID."""
        return repository.get_artist_by_id(artist_id=artist_id)

    @staticmethod
    def get_artist_by_username(username: str):
        """Gets an artist from the database by their username."""
        with SessionLocal() as db:
            try:
                repository = ArtistRepository(db)
                user = repository.get_artist_by_username(username=username)
                if user.role == "artist":
                    return user
            except Exception as e:
                raise e

    @staticmethod
    @repository_method_wrapper
    def get_all_artists(repository):
        """Gets all artists from the database."""
        return repository.get_all_artists()

    @staticmethod
    @repository_method_wrapper
    def delete_artist_by_id(repository, artist_id: str):
        """Deletes an artist from the database by their ID."""
        return repository.delete_artist_by_id(artist_id=artist_id)

    @staticmethod
    @repository_method_wrapper
    def update_artist_bio(repository, artist_id: str, bio: str):
        """Updates bio of an artist."""
        return repository.update_artist_bio(artist_id=artist_id, bio=bio)

    @staticmethod
    @repository_method_wrapper
    def update_artist_website(repository, artist_id: str, website: str):
        """Updates website of a customer."""
        return repository.update_artist_bio(artist_id=artist_id, website=website)
