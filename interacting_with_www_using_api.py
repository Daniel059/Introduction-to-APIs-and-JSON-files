# Connecting to an API iin python
import requests
# Make a GET request to the API
# The Guardians of the Galaxy Vol. 2
url = "http://www.omdbapi.com/?i=tt3896198&apikey=bd5a32f2"
r = requests.get(url)

json_data = r.json()
for key,value in json_data.items():
    print(f'{key} : {value}')