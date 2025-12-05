
import os, sys
<<<<<<< HEAD
 
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from flask import Flask, render_template, redirect, request, url_for
from movie_processing import getDataFromDB, getDataFromAPI, getMovie, searchMovieFromDb
=======
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from flask import Flask, render_template, redirect, request, session, url_for
from movie_processing import getDataFromDB, getDataFromAPI, getMovie, searchMovieFromDb
from login_process import createUser, login
from werkzeug.security import generate_password_hash, check_password_hash

>>>>>>> d891a53 (logini)

app = Flask(__name__)

app.secret_key = os.urandom(24)
@app.route("/")
def movies_homepage():
<<<<<<< HEAD
    allMovies = getDataFromDB()
    return render_template('home.html', movies = allMovies)
=======
    if "user_id" not in session:
        return redirect(url_for("signin"))
    allMovies = getDataFromDB()
    return render_template('home.html', movies=allMovies)
>>>>>>> d891a53 (logini)

@app.route("/movies/callapi")
def call_movies_api():
    getDataFromAPI()
    return redirect(url_for("movies_homepage"))
<<<<<<< HEAD

@app.route("/movies/<id>")
def movie_details(id):
    movie = getMovie(id)
    return render_template('movie_details.html', m = movie)


@app.route("/movies/", methods=["GET"])
def movies_search():
    search_query = request.args.get("search_query") 
    movies = searchMovieFromDb(search_query)
    return render_template('search_result.html', search_query = search_query, movies = movies)
=======

@app.route("/movies/<id>")
def movie_details(id):
    movie = getMovie(id)
    return render_template('movie_details.html', m = movie)


@app.route("/movies/", methods=["GET"])
def movies_search():
    search_query = request.args.get("search_query") 
    movies = searchMovieFromDb(search_query)
    return render_template('search_result.html', search_query = search_query, movies = movies)

@app.route("/login_page")
def signin_page():
    return render_template('login.html')
@app.route("/signup_page")
def signup_page():
    return render_template('signup.html')

@app.route("/login/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pwd")

        user = login(email, password)

        if user:
            session["user_id"] = user["id"]
            session["email"] = user["email"]
            return redirect(url_for("movies_homepage"))
        else:
            return render_template("login.html", error="Nom d'utilisateur ou mot de passe incorrect")

    return render_template("login.html")

@app.route("/signup/", methods=["GET"])
def signup():
    username = request.args.get("username") 
    email = request.args.get("email") 
    pwd = generate_password_hash(request.args.get("pwd") )
    createUser(username, email, pwd)
    return redirect(url_for("signin_page"))

@app.route("/logout/")
def logout():
    session.clear() 
    return redirect(url_for("signin"))
>>>>>>> d891a53 (logini)
