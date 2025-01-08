import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4608aeaf0428afa75fc1fe103f8ed643'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
body = {
    "pokemon_id": "185283"
}

respons=requests.post(url=f'{URL}/trainers/add_pokeball', json = body, headers=HEADER)

print(respons.text)