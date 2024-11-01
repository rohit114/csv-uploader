import os
from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.service.upload_service import process_csv_in_chunks
from app.utils.api_key_verify import verify_api_key

router = APIRouter()

@router.post("/upload/")
async def upload_csv(file: UploadFile, x_api_key: str = Depends(verify_api_key)):
    try:
        # Create a temporary file path
        file_path = f"tmp/{file.filename}"
        os.makedirs("tmp", exist_ok=True)  # Create tmp directory if it doesn't exist

        # Save the uploaded file to the temp location
        print("Loading... PID:", os.getpid())
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Process the CSV in chunks using the service
        process_csv_in_chunks(file_path)
        
        return {"status": "File uploaded and processed successfully."}
    except Exception as e:
        print(f"UPLOAD ERROR: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during the file upload.")
