# app/services/game_service.py

from datetime import date
from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.game import Game

def get_filtered_games(
    db: Session,
    age: Optional[int] = None,
    name: Optional[str] = None,
    release_date_gte: Optional[date] = None,
    release_date_lte: Optional[date] = None,
    limit: int = 10,
    offset: int = 0,
) -> List[Game]:
    query = db.query(Game)

    """
    Get games with optional filtering by age and name.
    Supports pagination with limit and offset.
    - age: Exact match for required_age.
    - name: Substring match for the game's name.
    - limit: Number of results per page.
    - offset: Number of items to skip.
    """
    # Filters based on query parameters
    if age is not None:
        query = query.filter(Game.required_age == age)
    if name is not None:
        query = query.filter(Game.name.ilike(f"%{name}%"))
    if release_date_gte is not None:
        query = query.filter(Game.release_date >= release_date_gte)
    if release_date_lte is not None:
        query = query.filter(Game.release_date <= release_date_lte)

    return query.offset(offset).limit(limit).all(), query.count()
