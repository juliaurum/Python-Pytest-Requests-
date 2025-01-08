import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4608aeaf0428afa75fc1fe103f8ed643'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
body = {
    "pokemon_id": "185283",
    "name": "Chip",
    "photo_id": 1
}

respons=requests.put(url=f'{URL}/pokemons', json = body, headers=HEADER)

print(respons.text)