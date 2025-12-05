from datetime import date
import requests
from api import api_secret
from db.oracle import db

url = 'http://www.omdbapi.com/?i=tt3896198&apikey='
api = url + api_secret.key
data = requests.get(api)
data = data.json()
getData = data

if(isinstance(getData, list)):
    data = getData
elif(isinstance(getData, dict)):
    data = [getData]

connection = db()
cursor = connection.cursor()

for i in data:
    movie = [
        i["imdbID"],
        i["Title"],
        i["Released"],
        int(i["Runtime"].strip(" min")),
        i["Genre"],
        i["Director"],
        i["Writer"],
        i["Actors"],
        i["Poster"],
        float(i["imdbRating"]),
        i["Language"],
        i["Plot"],
    ]
    cursor.execute("""
        INSERT INTO films (id, title, released, runtime, genre, director, writer, actors, poster_url, ratings, language, plot)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)
    """, movie)

connection.commit()
cursor.close()

print("insert success")



