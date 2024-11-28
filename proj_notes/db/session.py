from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from typing import Generator
from core.config import get_database_url


engine = create_engine(get_database_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()