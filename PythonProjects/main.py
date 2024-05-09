import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_creat = {
    "name": "generate",
    "photo": "generate"
}

body_change = {
    "pokemon_id": "26689",
    "name": "generate",
    "photo": "generate"
}

body_pokeball = {
    "pokemon_id": "26689"
}

response_creat = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat)
print(response_creat.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

