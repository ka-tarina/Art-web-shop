"""Module for category controller."""
from uuid import uuid4
from fastapi import HTTPException, Response
from app.artworks.exceptions import CategoryExceptionCode, CategoryNotFoundException
from app.artworks.services import CategoryService


class CategoryController:
    """A controller for handling requests related to category."""
    @staticmethod
    def create_new_category(name: str):
        """Creates a new category in the system."""
        try:
            category = CategoryService.create_category(name=name)
            return category
        except CategoryExceptionCode as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_categories():
        """Gets all categories from the database."""
        categories = CategoryService.get_all_categories()
        return categories

    @staticmethod
    def get_category_by_id(category_id: str):
        """Returns the category for the given id."""
        try:
            category = CategoryService.get_category_by_id(category_id)
            return category
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_category_by_name(name: str):
        """Gets a category from the database by its name."""
        try:
            category = CategoryService.get_category_by_name(name)
            return category
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_category_by_id(category_id: str):
        """Deletes a category from the database by their ID."""
        try:
            CategoryService.delete_category_by_id(category_id)
            return Response(
                content=f"Category with provided ID {category_id} was successfully deleted.",
                status_code=200,
            )
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_category_name(category_id: str, new_name: str):
        """Updates the name of the category."""
        try:
            category = CategoryService.update_category_name(category_id=category_id,
                                                            new_name=new_name)
            return category
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artworks_by_category_name(category_name: str, skip: int = 0, limit: int = 100):
        """Gets artwork by category name."""
        try:
            artworks = CategoryService.get_artworks_by_category_name(category_name=category_name,
                                                                     skip=skip,
                                                                     limit=limit)
            return artworks
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_artworks_by_category_id(category_id: str, skip: int = 0, limit: int = 100):
        """Gets artwork by category id."""
        try:
            artworks = CategoryService.get_artworks_by_category_id(category_id=category_id,
                                                                   skip=skip,
                                                                   limit=limit)
            return artworks
        except CategoryNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
