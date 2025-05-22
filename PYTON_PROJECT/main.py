import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '436c3632278bf912cc03578cde2ea365'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_post_pokemon={
      "name": "Moon1",
      "photo_id": -1
  
}



'''body_smena_imeni={
    "pokemon_id": pok_id,
    "name": "Moon4",
    "photo_id": -1
}

body_pokeball={
    "pokemon_id": pok_id
}'''


response=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_post_pokemon)
print(response.text)

pok_id=response.json()['id']
print(pok_id)

response_smena=requests.put(url=f'{URL}/pokemons', headers=HEADER, json={
    "pokemon_id": pok_id,
    "name": "Luna",
    "photo_id": -1
})
print(response_smena.text)

response_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json={
    "pokemon_id": pok_id
})
print(response_pokeball.text)

