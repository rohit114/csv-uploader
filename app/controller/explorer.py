
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Dict, Optional, List
from app.database import get_db
from app.models.game import Game
from app.response.game_response import GameListResponse
router = APIRouter()

@router.get("/games/", response_model=GameListResponse)
def get_games(
    age: Optional[int] = Query(None),
    name: Optional[str] = Query(None),
    release_date_gte: Optional[date] = Query(None),
    release_date_lte: Optional[date] = Query(None),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    """
    Get games with optional filtering by age and name.
    Supports pagination with limit and offset.
    - age: Exact match for required_age.
    - name: Substring match for the game's name.
    - limit: Number of results per page.
    - offset: Number of items to skip.
    """
    query = db.query(Game)

    #filters based on query parameters
    if age is not None:
        query = query.filter(Game.required_age == age)
    if name is not None:
        query = query.filter(Game.name.ilike(f"%{name}%"))
        
    # if release_date_gte is not None:
    #     query = query.filter(Game.release_date >= release_date_gte)
    # if release_date_lte is not None:
    #     query = query.filter(Game.release_date <= release_date_lte)

    #pagination
    games = query.offset(offset).limit(limit).all()
    total_games = query.count()

    #next offset calculation
    next_offset = offset + limit if offset + limit < total_games else None

    return {
        "games": games,
        "next_offset": next_offset,
    }

    