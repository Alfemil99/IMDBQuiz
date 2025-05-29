from flask import Blueprint, render_template, session, request, redirect, url_for
from app.models import Movie
from app.game import get_round_data
from app.leaderboard import insert_score, get_top_scores

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["score"] = 0
        return redirect(url_for("main.game"))
    return render_template("start.html")

@main.route("/movies")
def movie_list():
    movies = Movie.query.limit(20).all()
    return render_template("movies.html", movies=movies)


@main.route("/game")
def game():
    if "round" not in session or "round_score" not in session:
        session["round"] = get_round_data()
        session["hints_shown"] = 1        # første hint vises gratis
        session["round_score"] = 600

    round_data = session["round"]
    movie_ids = round_data["option_ids"]
    options = Movie.query.filter(Movie.id.in_(movie_ids)).all()
    options.sort(key=lambda m: movie_ids.index(m.id))

    return render_template("game.html",
                           round=round_data,
                           hints_shown=session.get("hints_shown", 1),
                           round_score=session.get("round_score", 600),
                           score=session.get("score", 0),
                           options=options)


@main.route("/reveal_hint")
def reveal_hint():
    if session.get("hints_shown", 1) < 5:
        session["round_score"] = session.get("round_score", 600) - 100
        session["hints_shown"] += 1
    return redirect(url_for("main.game"))


@main.route("/guess/<int:movie_id>")
def guess(movie_id):
    round_data = session.get("round")
    if not round_data:
        return redirect(url_for("main.game"))

    guess_correct = movie_id == round_data["correct_id"]

    if guess_correct:
        session["score"] = session.get("score", 0) + session.get("round_score", 0)
        session["result"] = "correct"
    else:
        session["result"] = "wrong"

    session["last_round"] = round_data
    session["last_guess"] = movie_id

    return redirect(url_for("main.result"))


@main.route("/result")
def result():
    round_data = session.get("last_round")
    guess_id = session.get("last_guess")
    result = session.get("result")
    score = session.get("score", 0)

    if not round_data or guess_id is None:
        return redirect(url_for("main.game"))

    movie_ids = round_data["option_ids"]
    options = Movie.query.filter(Movie.id.in_(movie_ids)).all()
    options.sort(key=lambda m: movie_ids.index(m.id))
    guessed_movie = next((m for m in options if m.id == guess_id), None)
    correct_movie = next((m for m in options if m.id == round_data["correct_id"]), None)

    if result == "wrong":
        final_score = score
        username = session.get("username", "Anonymous")
        insert_score(username, final_score)
        leaderboard = get_top_scores()
        session.clear()
        return render_template("gameover.html", score=final_score, correct_movie=correct_movie, leaderboard=leaderboard)



    # hvis korrekt → nulstil kun rundedata
    session.pop("round", None)
    session.pop("hints_shown", None)
    session.pop("round_score", None)
    session.pop("last_round", None)
    session.pop("last_guess", None)
    session.pop("result", None)

    return render_template("result.html",
                           result=result,
                           correct_movie=correct_movie)
