from app.db.database import SessionLocal
from app.users.repository import AdminRepository


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = AdminRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class AdminServices:
    @staticmethod
    @repository_method_wrapper
    def create_admin(repository, username, email, password):
        return repository.create_admin(username=username, email=email, password=password)

    @staticmethod
    @repository_method_wrapper
    def create_admin_from_existing_user(repository, user_id):
        return repository.create_admin_from_existing_user(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_admin_by_id(repository, admin_id):
        return repository.get_admin_by_id(superuser_id=admin_id)

    @staticmethod
    @repository_method_wrapper
    def get_all_admins(repository):
        return repository.get_all_admins()

    @staticmethod
    @repository_method_wrapper
    def delete_admin_by_id(repository, admin_id: str):
        return repository.delete_admin_by_id(superuser_id=admin_id)
