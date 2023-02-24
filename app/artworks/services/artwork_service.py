"""Module for artwork service."""
from uuid import uuid4
from app.artworks.repository import ArtworkRepository
from app.artworks.exceptions import ArtworkExceptionCode
from app.db import SessionLocal


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = ArtworkRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class ArtworkService:
    """A service for handling artwork."""
    @staticmethod
    def create_artwork(name: str,
                       description: str,
                       price: float,
                       image: str,
                       stock: int,
                       category_id: uuid4,
                       artist_id: uuid4):
        """Creates a new artwork in the system."""
        with SessionLocal() as db:
            try:
                repository = ArtworkRepository(db)
                if repository.artwork_exists(name, description):
                    raise ArtworkExceptionCode(
                        message="Artwork already exists in the database",
                        code=400
                    )
                return repository.create_artwork(
                    name=name,
                    description=description,
                    price=price,
                    image=image,
                    stock=stock,
                    category_id=category_id,
                    artist_id=artist_id
                )
            except Exception as e:
                raise e

    @staticmethod
    @repository_method_wrapper
    def get_artwork_by_id(repository, artwork_id: str):
        """Gets an artwork from the database by its id."""
        return repository.get_artwork_by_id(artwork_id=artwork_id)

    @staticmethod
    @repository_method_wrapper
    def get_artwork_by_name(repository, name: str):
        """Gets an artwork from the database by its name."""
        return repository.get_artwork_by_username(name=name)

    @staticmethod
    @repository_method_wrapper
    def update_artwork(repository, artwork_id: str, artwork_attribute: str, value):
        """Updates an attribute of the artwork."""
        return repository.update_artwork(artwork_id=artwork_id,
                                         artwork_attribute=artwork_attribute,
                                         value=value)

    @staticmethod
    @repository_method_wrapper
    def get_all_artworks(repository):
        """Gets all artworks from the database."""
        return repository.get_all_artworks()

    @staticmethod
    @repository_method_wrapper
    def get_stock_by_artwork_id(repository, artwork_id):
        """Gets stock of an artwork from the database by its id."""
        return repository.get_stock_by_artwork_id(artwork_id=artwork_id)

    @staticmethod
    @repository_method_wrapper
    def get_artworks_in_price_range(repository, min_price: float, max_price: float):
        """Returns a list of artworks within the given price range."""
        return repository.get_artworks_in_price_range(min_price=min_price, max_price=max_price)

    @staticmethod
    @repository_method_wrapper
    def delete_artwork_by_id(repository, artwork_id: str):
        """Deletes an artwork from the database by their ID."""
        return repository.delete_artwork_by_id(artwork_id=artwork_id)
