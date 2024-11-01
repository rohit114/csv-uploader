import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,              # Basic pool size (number of connections to keep open)
    max_overflow=30,           # Allow up to 30 additional connections beyond `pool_size`
    pool_timeout=120,           # Wait time (seconds) before a connection timeout
    pool_recycle=1800          # Recycle connections after 1800 seconds
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


