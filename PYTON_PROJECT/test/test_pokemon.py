import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '436c3632278bf912cc03578cde2ea365'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID='33539'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name_trainer():
    respons_name = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert respons_name.json()['data'][0]['trainer_name'] == 'Sunny' 