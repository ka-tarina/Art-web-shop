from app.db.database import SessionLocal
from app.users.repository import SuperUserRepository
from app.users.services import UserServices


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = SuperUserRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class SuperUserServices:
    @staticmethod
    @repository_method_wrapper
    def create_superuser(repository, username, email, password):
        return repository.create_superuser(username=username, email=email, password=password)

    # @staticmethod
    # @repository_method_wrapper
    # def create_superuser_from_existing_user(repository, user_id):
    #     return repository.create_superuser_from_existing_user(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_superuser_by_id(repository, superuser_id):
        return repository.get_superuser_by_id(superuser_id=superuser_id)

    @staticmethod
    @repository_method_wrapper
    def get_all_superusers(repository):
        return repository.get_all_superusers()

    @staticmethod
    @repository_method_wrapper
    def delete_superuser_by_id(repository, superuser_id: str):
        return repository.delete_superuser_by_id(superuser_id=superuser_id)
