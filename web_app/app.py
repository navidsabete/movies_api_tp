import os, sys
 
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from flask import Flask, render_template
from movie_processing import getDataFromDB, getMovie

app = Flask(__name__)

@app.route("/")
def movies_homepage():
    allMovies = getDataFromDB()
    return render_template('home.html', movies = allMovies)

@app.route("/movies/<id>")
def movie_details(id):
    movie = getMovie(id)
    return render_template('movie_details.html', m = movie)