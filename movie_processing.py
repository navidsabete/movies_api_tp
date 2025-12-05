
import oracledb
from api import api_secret
from db.oracle import db
import requests
from datetime import date

def getDataFromAPI():
    url = 'http://www.omdbapi.com/?apikey='
    api = url + api_secret.key + api_secret.search_title

    responseGetMovies = requests.get(api)
    print(responseGetMovies.json())
    # get all movie data
    getMovies = responseGetMovies.json()
    movie = getMovies["Search"]

    connection = db()
    cursor = connection.cursor()

    for m in movie:
        id = m["imdbID"]

        api_movie = f"http://www.omdbapi.com/?apikey={api_secret.key}&i={id}"
        getMovie = requests.get(api_movie).json()
        dataGetMovie = getMovie
        
        if(isinstance(dataGetMovie, list)):
            getMovie = dataGetMovie
        elif(isinstance(dataGetMovie, dict)):
            getMovie = [dataGetMovie]
        for mv in getMovie:
            movie = [
                mv["imdbID"],
                mv["Title"],
                int(mv["Year"]),
                int(mv["Runtime"].strip(" min")),
                mv["Genre"],
                mv["Director"],
                mv["Writer"],
                mv["Actors"],
                mv["Poster"],
                float(mv["imdbRating"]),
                mv["Language"],
                mv["Plot"]
            ]
            try:
                cursor.execute("""
                INSERT INTO films (id, title, released, runtime, genre, director, writer, actors, poster_url, ratings, language, plot)
                VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)
                """, movie)
            except oracledb.IntegrityError:
                print("Film déjà existant :", m["imdbID"])

    connection.commit()
    cursor.close()

def rows_to_dicts(cursor):
    columns = []
    for col in cursor.description:
        columns.append(col[0].lower())
    rows = []
    for row in cursor.fetchall():
        row_dict = {}
        for index, value in enumerate(row):
            row_dict[columns[index]] = value
        rows.append(row_dict)
    return rows


def getDataFromDB():
    connection = db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM films
        """)
    getFilms = rows_to_dicts(cursor)
    for f in getFilms:
        print(f)
    return getFilms

def getMovie(id):
    connection = db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE id = :id", {"id": id})
    getFilm = cursor.fetchone()
    columns = []
    for col in cursor.description:
        columns.append(col[0].lower())
    movie = dict(zip(columns, getFilm))
    return movie

def searchMovieFromDb(search = ''):
    search_sql = f'%{search}%'
    connection = db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE title LIKE :search", {"search": search_sql})
    getFilms = rows_to_dicts(cursor)
    for f in getFilms:
        print(f)
    return getFilms