import os, sys
 
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from flask import Flask, render_template, redirect, request, url_for
from movie_processing import getMoviesDataFromDB, getDataFromAPI, getMovieDataFromDB, searchMovieDataFromDB

app = Flask(__name__)

@app.route("/")
def movies_homepage():
    allMovies = getMoviesDataFromDB()
    return render_template('home.html', movies = allMovies)

@app.route("/movies/callapi")
def call_movies_api():
    getDataFromAPI()
    return redirect(url_for("movies_homepage"))

@app.route("/movies/<id>")
def movie_details(id):
    movie = getMovieDataFromDB(id)
    return render_template('movie_details.html', m = movie)


@app.route("/movies/", methods=["GET"])
def movies_search():
    search_query = request.args.get("search_query")
    print("Search query:", search_query) 
    movies = searchMovieDataFromDB(search_query)
    return render_template('search_results.html', search_query = search_query, movies = movies)