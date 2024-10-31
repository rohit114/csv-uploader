
#python3 -m venv venv
#source venv/bin/activate
#pip freeze > rclear
#uvicorn app.main:app --reload
from fastapi import FastAPI, HTTPException, UploadFile, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from multiprocessing import Pool
from .controller.upload import router as upload_router
from .database import Base, engine, get_db
from sqlalchemy.orm import Session
from .models.game import Game
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)

@app.get("/foo")
def getUsers(db: Session = Depends(get_db)):
    try:
        query = text("SELECT * FROM users")
        result = db.execute(query)
        users = [dict(row._mapping) for row in result]  # Use _mapping to get a dict-like object
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while f")
