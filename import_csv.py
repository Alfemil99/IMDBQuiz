import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Build DB connection string
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(db_url)

# Load and clean CSV
df = pd.read_csv("IMDB.csv", encoding="utf-8")

df = df.rename(columns={
    "Id": "id",
    "Poster_Link": "poster_link",
    "Series_Title": "title",
    "Released_Year": "year",
    "Certificate": "certificate",
    "Runtime": "runtime",
    "Genre": "genre",
    "IMDB_Rating": "imdb_rating",
    "Overview": "overview",
    "Meta_score": "meta_score",
    "Director": "director",
    "Star1": "star1",
    "Star2": "star2",
    "Star3": "star3",
    "Star4": "star4",
    "No_of_Votes": "votes",
    "Gross": "gross"
})

# Fix types
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

df["meta_score"] = pd.to_numeric(df["meta_score"], errors="coerce")
df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
df["imdb_rating"] = pd.to_numeric(df["imdb_rating"], errors="coerce")

# Upload to database (append only)
df.to_sql("movies", engine, if_exists="append", index=False)

print("CSV data added to movies table.")
