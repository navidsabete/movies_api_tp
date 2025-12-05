

import requests

from api import api_secret


url = 'http://www.omdbapi.com/?apikey='
api = url + api_secret.key + 's=a&page=2'

responseGetMovies = requests.get(api)

    # get all movie data
getMovies = responseGetMovies.json()
print(getMovies)