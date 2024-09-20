import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '877d5a73d53cde5e6a19121c6639c342'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}

body_create_pokemon = {
    "name": "qwert",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
id_pokemon = response.json()['id']
print(response.text)

new_name_pokemon = {
    "pokemon_id": id_pokemon,
    "name": "Qzaazaz",
    "photo_id": -1
}
response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = new_name_pokemon)
print(response_new_name.text)

add_pokeball = {
    "pokemon_id": id_pokemon
}
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(response_add_pokeball.text)