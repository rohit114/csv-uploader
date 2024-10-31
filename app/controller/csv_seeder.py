import csv
import random
from datetime import datetime, timedelta
import string

header = [
    "app_id", "name", "release_date", "required_age", "price", "dlc_count",
    "about_the_game", "supported_languages", "windows", "mac", "linux",
    "positive", "negative", "score_rank", "developers", "publishers",
    "categories", "genres", "tags"
]

sample_name = ["Galactic Bowling", "Space Wars", "Alien Strike", "Adventure Game"]
sample_languages = ["['English']", "['Spanish']", "['French']", "['German']"]
sample_categories = ["Single-player", "Multi-player"]
sample_genres = ["Indie", "Casual", "Sports"]
sample_tags = ["Indie", "Action", "Strategy"]

def generate_random_date(start_date="Jan 1, 2000", end_date="Dec 31, 2023"):
    start = datetime.strptime(start_date, "%b %d, %Y")
    end = datetime.strptime(end_date, "%b %d, %Y")
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime("%b %d, %Y")

def generate_unique_appid(existing_appids):
    # Generates a unique alphanumeric AppID in the format "ABC_12345"
    while True:
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = random.randint(10000, 99999)
        app_id = f"{letters}_{numbers}"
        if app_id not in existing_appids:
            existing_appids.add(app_id)
            return app_id

def generate_random_data(num_entries, start_id=1, output_file="smaller_sample.csv"):
    existing_appids = set()  # Track all generated AppIDs to prevent duplicates
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
        for i in range(start_id, start_id + num_entries):
            row = [
                # i,  # id
                generate_unique_appid(existing_appids),  # Unique alphanumeric AppID
                random.choice(sample_name),  # Name
                generate_random_date(),  # Release date
                random.choice([0, 13, 16]),  # Required age, fewer options
                round(random.uniform(0, 20), 2),  # Price range reduced
                random.randint(0, 2),  # DLC count, fewer options
                "Sample game description.",  # Shorter About the game
                random.choice(sample_languages),  # Supported languages
                random.choice(["TRUE", "FALSE"]),  # Windows
                random.choice(["TRUE", "FALSE"]),  # Mac
                random.choice(["TRUE", "FALSE"]),  # Linux
                random.randint(0, 1000),  # Positive, smaller range
                random.randint(0, 500),  # Negative, smaller range
                "",  # Score rank left empty
                "Sample Dev",  # Developers
                "Sample Pub",  # Publishers
                random.choice(sample_categories),  # Categories
                random.choice(sample_genres),  # Genres
                random.choice(sample_tags),  # Tags
            ]
            writer.writerow(row)
    print(f"{num_entries} entries written to {output_file}.")

# Generate around 1 million entries with reduced size
generate_random_data(100000, start_id=1, output_file="smaller_sample.csv")
