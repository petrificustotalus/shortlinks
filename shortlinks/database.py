import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlmodel import create_engine

ENV = os.getenv("ENV")


if ENV == "testing":
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5433/testdb"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://nnn:password@db:5432/shortlinks"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
