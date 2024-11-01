
#python3 -m venv venv
#source venv/bin/activate
#pip freeze > requirements.txt
#pip install -r requirements.txt
#uvicorn app.main:app --reload
#pytest -v app/tests/test_upload.py
#API doc http://localhost:8000/docs
from fastapi import FastAPI, HTTPException, UploadFile, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from multiprocessing import Pool
from .controller.upload import router as upload_router
from .controller.explorer import router as explorer_router
from .database import Base, engine, get_db
from sqlalchemy.orm import Session
from .models.game import Game
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)
app.include_router(explorer_router)

@app.get("/test")
def getUsers(db: Session = Depends(get_db)):
    try:
        query = text("SELECT * FROM users")
        result = db.execute(query)
        users = [dict(row._mapping) for row in result]  # Use _mapping to get a dict-like object
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while f")
