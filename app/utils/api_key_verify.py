# Load API key from environment
import os

from fastapi import HTTPException, Header
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")