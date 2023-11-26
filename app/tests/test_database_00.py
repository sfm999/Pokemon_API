import logging
import unittest
import requests
from random import randint
from database.pokemon_db import PokemonDatabase

FILENAME = "./data/pokemon.csv"

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class TestPokemonDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.db = PokemonDatabase(FILENAME)
        self.pokemons = self.db.read_pokemon_from_csv(FILENAME)

    def get_random_pokemon_index(self):
        return randint(0, 150)

    def test_read_pokemon_from_csv(self):
        test_db = PokemonDatabase(FILENAME)
        test_pokemons = test_db.read_pokemon_from_csv(filename=FILENAME)
        assert len(self.pokemons) == len(test_pokemons)
        for x in range(len(test_pokemons)):
            assert test_pokemons[x].compare_to(self.pokemons[x]), f"Inconsistency in pokemon database at array index of {x}"

    def test_get_pokemon_by_index(self):
        pokemon = self.db.pokemons[self.get_random_pokemon_index()]
        req = requests.get(url=f'http://127.0.0.1:8000/pokemon/index/{pokemon.index}')
        assert vars(pokemon) == req.json()

    def test_get_pokemon_by_name(self):
        pokemon = self.db.pokemons[self.get_random_pokemon_index()]
        req = requests.get(url=f'http://127.0.0.1:8000/pokemon/name/{pokemon.name}')
        assert vars(pokemon) == req.json()
