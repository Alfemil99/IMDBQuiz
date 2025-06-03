from app import db

# Define the Movie model representing rows in the 'movies' table
class Movie(db.Model):
    __tablename__ = 'movies'

    # Primary key column
    id = db.Column(db.Integer, primary_key=True)

    # Others
    poster_link = db.Column(db.Text)
    title = db.Column(db.Text)
    year = db.Column(db.Integer)
    certificate = db.Column(db.Text)
    runtime = db.Column(db.Text)
    genre = db.Column(db.Text)
    imdb_rating = db.Column(db.Float)
    overview = db.Column(db.Text)
    meta_score = db.Column(db.Integer)
    director = db.Column(db.Text)
    star1 = db.Column(db.Text)
    star2 = db.Column(db.Text)
    star3 = db.Column(db.Text)
    star4 = db.Column(db.Text)
    votes = db.Column(db.Integer)
    gross = db.Column(db.Text)


# Define a simple class to represent a leaderboard entry
class LeaderboardEntry:
    def __init__(self, data):
        self.id = data.get('id')
        self.username = data.get('username')
        self.score = data.get('score')
        self.played_at = data.get('played_at')
