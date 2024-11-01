# app/services/upload_service.py

import os
from multiprocessing import Pool, cpu_count
import pandas as pd
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database import get_db

num_worker = cpu_count() - 1  # Use one less than the number of available CPUs

def save_chunk_to_db(chunk: pd.DataFrame) -> bool:
    # Creating a new database session for this process
    db: Session = next(get_db())
    try:
        chunk.to_sql('games', con=db.get_bind(), if_exists='append', index=False)
        print("Chunk saved to the database successfully. PID:", os.getpid())
        return True  # Indicate success
    except Exception as e:
        print(f"Error occurred while saving chunk to DB: {e}")
        return False
    finally:
        db.close()  # Ensure the session is closed after processing

def process_single_chunk(chunk: pd.DataFrame) -> bool:
    # Process and save a single chunk to the database
    return save_chunk_to_db(chunk)

def process_csv_in_chunks(file_path: str, chunk_size: int = 10000):
    try:
        # Use a pool of processes
        with Pool(processes=num_worker) as pool:
            # Read the CSV in chunks
            results = []
            for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                # Process each chunk in parallel
                result = pool.apply_async(process_single_chunk, args=(chunk,))
                results.append(result)

            pool.close()  # No more tasks
            pool.join()   # Wait for all processes to finish
            
            # Check results
            for result in results:
                if not result.get():  # If any chunk failed to save
                    raise Exception("Failed to save at least one chunk to the database.")
    except Exception as e:
        print(f"Error occurred while processing CSV in chunks: {e}")
        raise HTTPException(status_code=500, detail="Failed to process CSV file.")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)  # Clean up the temp file
