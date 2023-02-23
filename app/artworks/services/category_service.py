"""Module for category service."""
from uuid import uuid4
from app.artworks.repository import CategoryRepository
from app.artworks.schemas import CategoryArtworksSchema
from app.db import SessionLocal


def repository_method_wrapper(func):
    """Automatically handles database sessions and exceptions."""
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = CategoryRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class CategoryService:
    """A service for handling category."""
    @staticmethod
    @repository_method_wrapper
    def create_category(repository, name: str):
        """Creates a new category in the system."""
        return repository.create_category(name=name)

    @staticmethod
    @repository_method_wrapper
    def get_category_by_id(repository, category_id: str):
        """Returns the category for the given id."""
        return repository.get_category_by_id(category_id=category_id)

    @staticmethod
    @repository_method_wrapper
    def get_category_by_name(repository, name: str):
        """Gets a category from the database by its name."""
        return repository.get_category_by_name(name=name)

    @staticmethod
    @repository_method_wrapper
    def update_category_name(repository, category_id: uuid4(), new_name: str):
        """Updates the name of the category."""
        return repository.update_category_name(category_id=category_id, new_name=new_name)

    @staticmethod
    @repository_method_wrapper
    def get_all_categories(repository):
        """Gets all categories from the database."""
        return repository.get_all_categories()

    @staticmethod
    @repository_method_wrapper
    def delete_category_by_id(repository, category_id: str):
        """Deletes a category from the database by their ID."""
        return repository.delete_category_by_id(category_id=category_id)

    @staticmethod
    def get_artworks_by_category_id(category_id: str, skip: int = 0, limit: int = 100):
        """Gets artwork by category id."""
        with SessionLocal() as db:
            try:
                category = CategoryRepository(db).get_category_by_id(category_id=category_id)
                return CategoryArtworksSchema(name=category.name, artworks=category.artworks)
            except Exception as e:
                raise e

    @staticmethod
    def get_artworks_by_category_name(category_name: str, skip: int = 0, limit: int = 100):
        """Gets artwork by category name."""
        with SessionLocal() as db:
            try:
                category = CategoryRepository(db).get_category_by_name(name=category_name)
                return CategoryArtworksSchema(name=category.name, artworks=category.artworks)
            except Exception as e:
                raise e
