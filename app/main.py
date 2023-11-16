#!/usr/bin/python3

from fastapi import FastAPI
from typing import Optional
from app.database.pokemon_db import PokemonDatabase
from app.models.pokemon import Pokemon

app = FastAPI()
db = PokemonDatabase('./app/data/pokemon.csv')

@app.get("/pokemon/index/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: Optional[int] = None):
    """Takes an index of a pokemon and returns the pokemon or http status code 400"""
    if pokemon_id:
        return db.get_pokemon_by_index(index=pokemon_id)

@app.get("/pokemon/name/{pokemon_name}")
def get_pokemon_by_name(pokemon_name: Optional[str] = None):
    """Takes the name of a pokemon and returns the pokemon or http status code 400"""
    if pokemon_name:
        return db.get_pokemon_by_name(name=pokemon_name)
