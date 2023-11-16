import requests
from random import randint
from app.database.pokemon_db import PokemonDatabase

filename = "./app/data/pokemon.csv"
db = PokemonDatabase(filename)
pokemons = db.read_pokemon_from_csv(filename)

def get_random_pokemon_index():
    return randint(0, 150)

def test_read_pokemon_from_csv():
    test_db = PokemonDatabase(filename)
    test_pokemons = test_db.read_pokemon_from_csv(filename=filename)
    assert len(pokemons) == len(test_pokemons)
    for x in range(len(test_pokemons)):
        assert test_pokemons[x].compare_to(pokemons[x]), f"Inconsistency in pokemon database at array index of {x}"

def test_get_pokemon_by_index():
    pokemon = db.pokemons[get_random_pokemon_index()]
    req = requests.get(url=f'http://127.0.0.1:8000/pokemon/index/{pokemon.index}')
    assert vars(pokemon) == req.json()

def test_get_pokemon_by_name():
    pokemon = db.pokemons[get_random_pokemon_index()]
    req = requests.get(url=f'http://127.0.0.1:8000/pokemon/name/{pokemon.name}')
    assert vars(pokemon) == req.json()
