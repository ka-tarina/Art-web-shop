from pydantic import EmailStr
from app.db.database import SessionLocal
import hashlib
from app.users.exceptions import UserInvalidPassword
from app.users.models import UserStatus
from app.users.repository import UserRepository


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = UserRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class UserServices:
    @staticmethod
    def create_user(username, email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(username=username, email=email, password=hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    @repository_method_wrapper
    def get_user_by_id(repository, user_id: str):
        return repository.get_category_by_id(user_id=user_id)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username(repository, username: str):
        return repository.get_user_by_username(username=username)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username_or_id(repository, username_or_id: str):
        return repository.get_user_by_username_or_id(username_or_id=username_or_id)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_email(repository, email: EmailStr):
        return repository.read_user_by_email(email=email)

    @staticmethod
    @repository_method_wrapper
    def get_user_by_username_or_id_or_email(repository, username_id_email: str):
        return repository.get_user_by_username_or_id_or_email(username_id_email=username_id_email)

    @staticmethod
    @repository_method_wrapper
    def update_user_email(repository, email: EmailStr, new_email: EmailStr):
        return repository.update_user_email(email=email, new_email=new_email)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return hashed_password == hashlib.sha256(bytes(plain_password, "utf-8")).hexdigest()

    @staticmethod
    @repository_method_wrapper
    def update_user_password(repository, email: EmailStr, password: str, new_password: str):
        user = repository.read_user_by_email(email=email)
        if not repository.check_password(user_id=user.email, password=password):
            raise ValueError("Invalid old password")
        hashed_password = hashlib.sha256(bytes(new_password, 'utf-8')).hexdigest()
        return repository.update_user_password(email=email, new_password=hashed_password)

    @staticmethod
    @repository_method_wrapper
    def update_user_status(repository, username_id_email: str, status: UserStatus):
        return repository.update_user_status(username_id_email=username_id_email, status=status)

    @staticmethod
    @repository_method_wrapper
    def update_user_role(repository, username_id_email: str, role: UserStatus):
        return repository.update_user_role(username_id_email=username_id_email, role=role)

    @staticmethod
    @repository_method_wrapper
    def get_all_users(repository):
        return repository.get_all_users()

    @staticmethod
    @repository_method_wrapper
    def delete_user_by_id(repository, user_id: str):
        return repository.delete_user_by_id(user_id=user_id)

    @staticmethod
    def login_user(email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email=email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
