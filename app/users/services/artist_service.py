from app.db.database import SessionLocal
from app.users.repository import ArtistRepository


def repository_method_wrapper(func):
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
    def create_artist(repository, username: str, email: str, password: str):
        """Creates a new artist in the system."""
        return repository.create_artist(username, email, password)

    @staticmethod
    @repository_method_wrapper
    def get_artist_by_id(repository, artist_id: str):
        """Gets an artist from the database by their ID."""
        return repository.get_artist_by_id(artist_id)

    @staticmethod
    @repository_method_wrapper
    def get_artist_by_username(repository, username: str):
        """Gets an artist from the database by their username."""
        return repository.get_artist_by_username(username)

    @staticmethod
    @repository_method_wrapper
    def get_all_artists(repository):
        """Gets all artists from the database."""
        return repository.get_all_artists()

    @staticmethod
    @repository_method_wrapper
    def delete_artist_by_id(repository, artist_id: str):
        """Deletes an artist from the database by their ID."""
        return repository.delete_artist_by_id(artist_id)

    @staticmethod
    @repository_method_wrapper
    def update_artist_bio(repository, artist_id: str, bio: str):
        """Updates bio of an artist."""
        return repository.update_artist_bio(artist_id, bio)

    @staticmethod
    @repository_method_wrapper
    def update_artist_website(repository, artist_id: str, website: str):
        """Updates website of a customer."""
        return repository.update_artist_bio(artist_id, website)
