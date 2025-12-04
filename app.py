from api import api_secret
import requests

url = 'http://www.omdbapi.com/?i=tt3896198&apikey='
api = url + api_secret.key

data = requests.get(api)

print(data.json())



