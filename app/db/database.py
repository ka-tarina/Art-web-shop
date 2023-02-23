"""
Module creates a database session and an engine
object for connecting to the MySQL database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

if settings.USE_TEST_DB:
    db_name = settings.DB_NAME_TEST
else:
    db_name = settings.DB_NAME

MYSQL_URL = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@" \
            f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{db_name}"

engine = create_engine(MYSQL_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


def get_db():
    """A generator function that returns a database session object."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
