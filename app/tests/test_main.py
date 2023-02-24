"""Module for main Test Class"""
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.db import Base
from app.main import app

MYSQL_URL_TEST = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@" \
                 f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME_TEST}"

engine = create_engine(MYSQL_URL_TEST, echo=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)


class TestClass:
    """Test class setup and teardown"""

    def setup_method(self):
        """setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        Base.metadata.create_all(bind=engine)

    def teardown_method(self):
        """teardown any state that was previously setup with a setup_method
        call.
        """
        Base.metadata.drop_all(bind=engine)
