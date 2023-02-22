"""Module for category repository."""
from uuid import uuid4
from sqlalchemy import orm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload
from app.artworks.models import Category


class CategoryRepository:
    """A repository class for Category models."""
    def __init__(self, db: Session):
        """Initializes a new instance of the CategoryRepository class."""
        self.db = db

    def create_category(self, name):
        """Creates a new category in the system."""
        try:
            category = Category(name=name)
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            self.db.expunge(category)
            category = self.db.query(Category).\
                options(joinedload(Category.artworks)).get(category.id)
            return category
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Category with this name already exists.")

    def get_category_by_id(self, category_id: uuid4()):
        """Returns the category for the given id."""
        category = self.db.query(Category).\
            options(orm.joinedload('artworks')).filter_by(id=category_id).first()

        if category is None:
            raise ValueError(f"Category with id '{category_id}' does not exist.")
        self.db.add(category)
        self.db.refresh(category)
        return category

    def get_category_by_name(self, name: str):
        """Gets a category from the database by its name."""
        category = self.db.query(Category).filter(Category.name == name).first()
        if not category:
            raise ValueError("Category not found.")
        return category

    def get_all_categories(self):
        """Gets all categories from the database."""
        categories = self.db.query(Category).options(joinedload(Category.artworks)).all()
        return categories

    def update_category_name(self, category_id: uuid4, new_name: str):
        """Updates the name of the category."""
        category = self.get_category_by_id(category_id=category_id)
        category.name = new_name
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete_category_by_id(self, category_id: str):
        """Deletes a category from the database by their ID."""
        category = self.get_category_by_id(category_id)
        if not category:
            return None
        self.db.delete(category)
        self.db.commit()
