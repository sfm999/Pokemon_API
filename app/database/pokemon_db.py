import csv
from fastapi import HTTPException
from app.models.pokemon import Pokemon

class PokemonDatabase:
    
    last_index = -1
    pokemons = None

    def __init__(self, csv_filename: str):
        self.pokemons = self.read_pokemon(filename=csv_filename)
        self.last_index = len(self.pokemons)-1

    def read_pokemon(self, filename: str):
        """ Read in csvFile and create list of pokemon from it"""
        pokemon = list()
        with open(filename, newline='') as csvfile:
            csv_pokemon = csv.reader(csvfile, delimiter=',')
            next(csv_pokemon)
            for row in csv_pokemon:
                pokemon.append(Pokemon(*row))
        
        return pokemon
    
    def get_pokemon_by_id(self, index: int):
        if self.last_index >= 0 and index-1 <= self.last_index and index - 1 >= 0:
            return self.pokemons[index-1]
        else:
            return HTTPException(status_code=400, detail="Pokemon not found under that index")
        
    def get_pokemon_by_name(self, name: str):
        name = name.lower()
        for pokemon in self.pokemons:
            if pokemon.name.lower() == name:
                return pokemon
        return HTTPException(status_code=400, detail="Pokemon not found under that name")
