import random
from app.models import Movie
from app import db

def _pick_four_movies():
    """
    Vælger én korrekt film og tre tilfældige forkerte.
    """
    total = db.session.query(Movie).count()
    correct = db.session.query(Movie).offset(random.randrange(total)).first()

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
    Returnerer 5 hints baseret på filmen.
    """
    return [
        f"Released in {movie.year}",
        f"IMDB Rating {movie.imdb_rating}",
        f"Top-billed actor: {movie.star1}",
        f"Director: {movie.director}",
        f"Genre: {movie.genre}",
    ]

def get_round_data():
    """
    Returnerer data for en runde – kun JSON-venligt!
    """
    correct, wrongs = _pick_four_movies()
    options = wrongs + [correct]
    random.shuffle(options)

    return {
        "correct_id": correct.id,
        "hints": _generate_hints(correct),
        "option_ids": [m.id for m in options]
    }

