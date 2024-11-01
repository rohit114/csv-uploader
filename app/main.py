
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
from .controller.upload_controller import router as upload_router
from .controller.explorer_controller import router as explorer_router
from .database import Base, engine, get_db
from sqlalchemy.orm import Session
from .models.game import Game
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)
app.include_router(explorer_router)
