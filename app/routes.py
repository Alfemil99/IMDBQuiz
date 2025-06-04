from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app.models import Movie
from app.game import get_round_data
from app.leaderboard import insert_score, get_top_scores
import re

main = Blueprint("main", __name__)

@main.route("/")
def index():
    # Display the homepage with the leaderboard
    leaderboard = get_top_scores()
    return render_template("index.html", leaderboard=leaderboard)

@main.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        username = request.form.get("username", "").strip()

        # Validate only letters and spaces, 2–30 characters long
        if not re.match(r'^[A-Za-zÆØÅæøå\s]{2,30}$', username):
            flash("The name must only contain letters and be 2–30 characters long.")
            return redirect(url_for("main.index"))

        # Save username and reset score
        session["username"] = username
        session["score"] = 0
        return redirect(url_for("main.game"))
    
    # Show the start screen
    return render_template("start.html")


@main.route("/game")
def game():
    # If no username in session, redirect to start page
    if "username" not in session:
        return redirect(url_for("main.index"))

    # If no current round, initialize a new one
    if "round" not in session or "round_score" not in session:
        session["round"] = get_round_data()
        session["hints_shown"] = 1        # Show first hint for free
        session["round_score"] = 600      # Start score for the round

    round_data = session["round"]
    movie_ids = round_data["option_ids"]
    options = Movie.query.filter(Movie.id.in_(movie_ids)).all()
    options.sort(key=lambda m: movie_ids.index(m.id))

    # Render the game screen
    return render_template("game.html",
                           round=round_data,
                           hints_shown=session.get("hints_shown", 1),
                           round_score=session.get("round_score", 600),
                           score=session.get("score", 0),
                           options=options)


@main.route("/reveal_hint")
def reveal_hint():
    # Show an additional hint if fewer than 5 shown
    if session.get("hints_shown", 1) < 5:
        session["round_score"] = session.get("round_score", 600) - 100
        session["hints_shown"] += 1
    return redirect(url_for("main.game"))


@main.route("/guess/<int:movie_id>")
def guess(movie_id):
    round_data = session.get("round")
    if not round_data:
        return redirect(url_for("main.game"))
    
    # Check if the guessed movie is correct
    guess_correct = movie_id == round_data["correct_id"]

    if guess_correct:
        # Add round score to total score
        session["score"] = session.get("score", 0) + session.get("round_score", 0)
        session["result"] = "correct"
    else:
        session["result"] = "wrong"

     # Save last round and guess for result screen
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

    # Identify guessed and correct movies
    guessed_movie = next((m for m in options if m.id == guess_id), None)
    correct_movie = next((m for m in options if m.id == round_data["correct_id"]), None)

    if result == "wrong":
        # Game over: save score and show leaderboard
        final_score = score
        username = session.get("username", "Anonymous")
        insert_score(username, final_score)
        leaderboard = get_top_scores()
        session.clear()
        return render_template("gameover.html", score=final_score, correct_movie=correct_movie, leaderboard=leaderboard)

    # If correct guess, clear only round-related session data
    session.pop("round", None)
    session.pop("hints_shown", None)
    session.pop("round_score", None)
    session.pop("last_round", None)
    session.pop("last_guess", None)
    session.pop("result", None)

    return render_template("result.html",
                           result=result,
                           correct_movie=correct_movie)
@main.route("/reset")
def reset():
    session.clear()  # Resets Game
    return redirect(url_for("main.index"))