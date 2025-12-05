
import os, sys
 
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from flask import Flask, render_template, redirect, request, url_for
from movie_processing import getDataFromDB, getDataFromAPI, getMovie, searchMovieFromDb

app = Flask(__name__)

@app.route("/")
def movies_homepage():
    allMovies = getDataFromDB()
    return render_template('home.html', movies = allMovies)

@app.route("/movies/callapi")
def call_movies_api():
    getDataFromAPI()
    return redirect(url_for("movies_homepage"))

@app.route("/movies/<id>")
def movie_details(id):
    movie = getMovie(id)
    return render_template('movie_details.html', m = movie)


@app.route("/movies/", methods=["GET"])
def movies_search():
    search_query = request.args.get("search_query") 
    movies = searchMovieFromDb(search_query)
    return render_template('search_result.html', search_query = search_query, movies = movies)