from pydantic import BaseModel
from typing import List, Optional

class GameResponse(BaseModel):
    id: int
    app_id: str
    name: str
    release_date: Optional[str] = None
    required_age: Optional[int] = None
    price: Optional[float] = None
    dlc_count: Optional[int] = None
    about_the_game: Optional[str] = None
    supported_languages: Optional[str] = None
    windows: Optional[bool] = None
    mac: Optional[bool] = None
    linux: Optional[bool] = None
    positive: Optional[int] = None
    negative: Optional[int] = None
    score_rank: Optional[int] = None
    developers: Optional[str] = None
    publishers: Optional[str] = None
    categories: Optional[str] = None
    genres: Optional[str] = None
    tags: Optional[str] = None

    class Config:
        orm_mode = True  # This tells Pydantic to convert from ORM objects

class GameListResponse(BaseModel):
    games: List[GameResponse]
    next_offset: Optional[int]
