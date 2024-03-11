from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import database_settings

SQLALCHEMY_DATABASE_URL = database_settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

from typing import Generator

def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield db
  finally:
     db.close()  
