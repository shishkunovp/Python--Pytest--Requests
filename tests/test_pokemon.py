import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '877d5a73d53cde5e6a19121c6639c342'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}

trainer_id = '5585'
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response_get.json()["data"][0]["id"] == trainer_id


    