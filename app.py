from api import api_secret
from db.oracle import db

url = 'http://www.omdbapi.com/?i=tt3896198&apikey='
api = url + api_secret.key

data = []

connection = db()
cursor = connection.cursor()

cursor.executemany("""
    INSERT INTO films (id, title, release, runtime, genre, director, writer, actors, poster_url, rating, language, plot)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
""", data)

connection.commit()
cursor.close()

print("insert success")



