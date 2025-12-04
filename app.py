from api import api_secret
from db.oracle import db
import requests
from datetime import date

url = 'http://www.omdbapi.com/?i=tt3896198&apikey='
api = url + api_secret.key

responseGetMovies = requests.get(api)

# get all movie data
getMovies = responseGetMovies.json()

dataGetMovies = getMovies
if(isinstance(dataGetMovies, list)):
    getMovies = dataGetMovies
elif(isinstance(dataGetMovies, dict)):
    getMovies = [dataGetMovies]

movie = []


connection = db()
cursor = connection.cursor()

for m in getMovies:
    print(m)
    movie = [
        m["imdbID"],
        m["Title"],
        date.strptime(m["Released"], '%d %B %Y'),
        int(m["Runtime"].strip(" min")),
        m["Genre"],
        m["Director"],
        m["Writer"],
        m["Actors"],
        m["Poster"],
        float(m["imdbRating"]),
        m["Language"],
        m["Plot"]
    ]
    cursor.execute("""
    INSERT INTO films (id, title, released, runtime, genre, director, writer, actors, poster_url, ratings, language, plot)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)
    """, movie)

connection.commit()
cursor.close()