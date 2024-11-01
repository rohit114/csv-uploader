# from datetime import date
# from pydantic import BaseModel
# from typing import List, Optional

# from sqlalchemy import Date

from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class GameResponse(BaseModel):
    id: int
    app_id: str
    name: str
    release_date: date
    required_age: int
    price: float
    dlc_count: int
    about_the_game: Optional[str] = None
    supported_languages: Optional[str] = None
    windows: bool
    mac: bool
    linux: bool
    positive: int
    negative: int
    score_rank: int
    developers: Optional[str] = None
    publishers: Optional[str] = None
    categories: Optional[str] = None
    genres: Optional[str] = None
    tags: Optional[str] = None

    class Config:
        from_attributes = True  # This tells Pydantic to convert from ORM objects

class GameListResponse(BaseModel):
    games: List[GameResponse]
    next_offset: Optional[int]


# class GameResponse(BaseModel):
#     id: int
#     app_id: str
#     name: str
#     release_date: date
#     required_age: int
#     price: float
#     dlc_count: int
#     about_the_game: str
#     supported_languages: str
#     windows: bool
#     mac: bool
#     linux: bool
#     positive: int
#     negative: int
#     score_rank: int
#     developers: str
#     publishers: str
#     categories: str
#     genres: str
#     tags: str

#     class Config:
#         from_attributes = True  # This tells Pydantic to convert from ORM objects

# class GameListResponse(BaseModel):
#     games: List[GameResponse]
#     next_offset: Optional[int]
