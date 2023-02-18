from app.artworks.repository import CategoryRepository
from app.db import SessionLocal


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = CategoryRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class CategoryService:
    @staticmethod
    @repository_method_wrapper
    def create_category(repository, name: str):
        return repository.create_category(name=name)

    @staticmethod
    @repository_method_wrapper
    def get_category_by_id(repository, category_id: str):
        return repository.get_category_by_id(category_id=category_id)

    @staticmethod
    @repository_method_wrapper
    def get_category_by_name(repository, name: str):
        return repository.get_category_by_username(name=name)

    @staticmethod
    @repository_method_wrapper
    def update_category_name(repository, category_id: str, new_name: str):
        return repository.update_category_name(category_id=category_id, new_name=new_name)

    @staticmethod
    @repository_method_wrapper
    def get_all_categories(repository):
        return repository.get_all_categories()

    @staticmethod
    @repository_method_wrapper
    def delete_category_by_id(repository, category_id: str):
        return repository.delete_category_by_id(category_id=category_id)

    @staticmethod
    def get_artworks_by_category_id(category_id: str, skip: int = 0, limit: int = 100):
        with SessionLocal() as db:
            try:
                category = CategoryRepository(db).get_category_by_id(category_id=category_id)
                return category.artworks[skip: skip + limit]
            except Exception as e:
                raise e

    @staticmethod
    def get_artworks_by_category_name(category_name: str, skip: int = 0, limit: int = 100):
        with SessionLocal() as db:
            try:
                category = CategoryRepository(db).get_category_by_name(category_name=category_name)
                return category.artworks[skip: skip + limit]
            except Exception as e:
                raise e
