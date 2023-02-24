"""Model for Test user repository"""
from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository


class TestUserRepo(TestClass):
    """Test Class"""

    def create_users_for_methods(self):
        """Method for creation of users for method"""
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user_repository.create_user("user1", "user1@gmail.com", "sifra123")
            user_repository.create_user("user2", "user2@gmail.com", "sifra123")
            user_repository.create_user("user3", "user3@gmail.com", "sifra123")
            user_repository.create_user("user4", "user4@gmail.com", "sifra123")

    def test_get_all_users(self):
        """Test for getting all users"""
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        """Test for getting all users error"""
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert not len(all_users) != 4

    def test_get_user_by_id(self):
        """Test for getting user by id."""
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert user == user1

    def test_get_user_by_id_error(self):
        """Test for getting user by id error."""
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert not user != user1

    def test_delete_user_by_id(self):
        """Test for deleting user"""
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            assert user_repository.delete_user_by_id(user.id) is True

    def test_delete_user_by_id_error(self):
        """Test for deleting user error"""
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user5", "user5@gmail.com", "sifra1253")
            assert user_repository.delete_user_by_id(user.id) is not False
