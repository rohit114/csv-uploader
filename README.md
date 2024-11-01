# CSV Uploader API

## About

The CSV Uploader API is a FastAPI-based application designed to facilitate the uploading of CSV files containing massive data (100MB+). This application supports bulk import from csv to relational db, using multiprocessing for parallel processing (speed depends on CPU core), and allows querying for information with various filters. Built with modern technologies, it provides a robust backend solution for managing data and exploring data.

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
   `NOTE: 1. rename sample.env to .env ->  add DATABASE_URL, API_KEY **`
   `NOTE: 2. create databse in postgres as per DATABASE_URL`

   ```bash
   uvicorn app.main:app --reload

## Docker Setup
   * `docker-compose build`
   * `docker-compose up`
   * Application will listen to PORT as per exposed PORT docker-compose file

### API Documentation
   
   1. Generate CSV data 10 Lakh records (around 160MB) sample_data.csv
      * `python3 app/utils/csv_seeder.py`

   2. Uplaod csv
      * About:
         * make sure to create a database as per POSTGRES_DB `.env` file
         * can support large csv file (tested locally with 10 Lakh records, takes around 17-20 seconds ( 8 core CPU) to bulk insert in table )

      * METHOD: `POST`
      * URL: `{{BASE_URL}}/upload/`
      * HEADER: `x_api_key: xxxxxxx` as per `.env`, `Content-Type : multipart/form-data`
      * BODY: `form-data : key=file, value= attach sample_data.csv (generated in step 1)`
      * api will return `200 OK  { "status": "File uploaded and processed successfully."}` on success else throw error

   3. Explore Game data:
      * METHOD: `GET`
      * URL: `{{BASE_URL}}/games/?limit=10&offset=0`
      * HEADER: `x_api_key` as per sample.env file
       * Query Params:
         * `limit (optional default 10)`
         * `offset (optional default 0)`
         * `name (optional)`
         * `age (optional)`
         * `release_date_gte (optional)`
         * `release_date_lte (optional)`
      * api will return `200 OK { "data": [list of games], "next_offset": 10 }`

   4. Refer for more
      * API doc: http://{HOST}:{PORT}/docs | local : (http://localhost:8000/docs)

### Contact
* email me at rohitkumardas114@gmail.com for support or reporting any issues