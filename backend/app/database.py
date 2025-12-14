import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DB_FILE  # relative import is correct

db_path = os.path.abspath(DB_FILE)
DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
