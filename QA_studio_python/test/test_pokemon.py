import requests

URL = "https://api.pokemonbattle.ru"

HEADER = {"Content-Type" : "application/json"}

def test_get_traners():
    """
    KTI-1. Get traners
    """
response=requests.get(url=f"{URL}/v2/trainers", params={"trainer_id":"25085"},headers=HEADER,timeout=5)

assert response.status_code == 200, "Unexpected status code"