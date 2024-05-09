import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TRAINER_ID = '2636'

def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers')
    assert response_trainers.status_code == 200


def test_trainer_name():
    response_get_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get_name.json()["data"][0]["trainer_name"] == "Nikita"

