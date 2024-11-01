
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Any, Dict, Optional, List
from app.database import get_db
from app.models.game import Game
from app.response.game_response import GameListResponse
from app.service.game_explorer_service import get_filtered_games
from app.utils.api_key_verify import verify_api_key
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
    x_api_key: str = Depends(verify_api_key)
):
    
    """
    Get games with optional filtering by age and name, release_date.
    Supports pagination with limit and offset.
    """
    games, total_games = get_filtered_games(
        db,
        age=age,
        name=name,
        release_date_gte=release_date_gte,
        release_date_lte=release_date_lte,
        limit=limit,
        offset=offset,
    )


    #next offset calculation
    next_offset = offset + limit if offset + limit < total_games else None

    return {
        "games": games,
        "next_offset": next_offset,
    }
    
@router.get("/test")
def testRarQuery(db: Session = Depends(get_db)):
    try:
        query = text("SELECT * FROM games LIMIT 5")
        result = db.execute(query)
        games = [dict(row._mapping) for row in result]
        return games
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while f")

    