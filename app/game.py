import random
from app.models import Movie
from app import db

def _pick_four_movies():
    """
    Picks one correct movie and three random incorrect ones
    """
    # Get the total number of movies in the database
    total = db.session.query(Movie).count()

    # Select one random movie to be the correct answer
    correct = db.session.query(Movie).offset(random.randrange(total)).first()

    # Select three random movies that are not the correct one
    wrong = (
        db.session.query(Movie)
        .filter(Movie.id != correct.id)
        .order_by(db.func.random())
        .limit(3)
        .all()
    )

    return correct, wrong



def _generate_hints(movie: Movie) -> list[str]:
    """
    Returns 5 hints based on the movie
    """
    # Create and return a list of simple hints
    return [
        f"Released in {int(movie.year)}",
        f"Gross: {movie.gross}$",
        f"Top-billed actor: {movie.star1}",
        f"Director: {movie.director}",
        f"Genre: {movie.genre}",
    ]



def get_round_data():
    """
    Returns data for one round – JSON-friendly only
    """
    # Pick one correct movie and three incorrect ones
    correct, wrongs = _pick_four_movies()

    # Combine and shuffle all movie options
    options = wrongs + [correct]
    random.shuffle(options)

    # Return the round data in a JSON-compatible format
    return {
        "correct_id": correct.id,
        "hints": _generate_hints(correct),
        "option_ids": [m.id for m in options]
    }

