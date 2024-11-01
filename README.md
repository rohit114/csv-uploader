# CSV Uploader API

## About

The CSV Uploader API is a FastAPI-based application designed to facilitate the uploading of CSV files containing game data. This application supports bulk uploads, processes the data efficiently using background tasks, and allows querying for game information with various filters. Built with modern technologies, it provides a robust backend solution for managing game data.

## Tech Stack

- **FastAPI**: A modern web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **PostgreSQL**: A powerful, open-source relational database system known for its reliability, feature robustness, and performance.
- **SQLAlchemy ORM**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python, providing a full suite of well-known enterprise-level persistence patterns.

## Local Setup

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohit114/csv-uploader.git
   cd csv-uploader

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv

3. **Activate virtual environment**:
   ```bash
   (Linux/Mac)
   source venv/bin/activate 
   
   (Windows)
   venv\Scripts\activate

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

6. **Run Application**:
   ```bash
   uvicorn app.main:app --reload


## API Documentation
   API doc: (http://localhost:8000/docs)

