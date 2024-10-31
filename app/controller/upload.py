

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name} !!!!"}

@router.get("/foo2")
def getUsers(db: Session = Depends(get_db)):
    try:
        query = text("SELECT * FROM users")
        result = db.execute(query)
        users = [dict(row._mapping) for row in result]  # Use _mapping to get a dict-like object
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while f")
