import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository


class TestUserRepo(TestClass):

    def create_users_for_methods(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user_repository.create_user("user1", "user1@gmail.com", "sifra123")
            user_repository.create_user("user2", "user2@gmail.com", "sifra123")
            user_repository.create_user("user3", "user3@gmail.com", "sifra123")
            user_repository.create_user("user4", "user4@gmail.com", "sifra123")

    def test_get_all_users(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert not len(all_users) != 4

    def test_get_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert user == user1

    def test_get_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert not user != user1

    def test_delete_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            assert user_repository.delete_user_by_id(user.id) is True

    def test_delete_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            assert user_repository.delete_user_by_id(user.id) is not False
