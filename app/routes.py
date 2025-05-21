from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

from flask import render_template
from app.models import Movie

@main.route("/movies")
def movie_list():
    movies = Movie.query.limit(20).all()
    return render_template("movies.html", movies=movies)