from sqlalchemy import Column, Date, Integer, String, Float, Boolean

from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(String, unique=True, index=True)
    name = Column(String)
    release_date = Column(Date)
    required_age = Column(Integer)
    price = Column(Float)
    dlc_count = Column(Integer)
    about_the_game = Column(String)
    supported_languages = Column(String)
    windows = Column(Boolean)
    mac = Column(Boolean)
    linux = Column(Boolean)
    positive = Column(Integer)
    negative = Column(Integer)
    score_rank = Column(Integer)
    developers = Column(String)
    publishers = Column(String)
    categories = Column(String)
    genres = Column(String)
    tags = Column(String)
