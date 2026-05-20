import json

with open("pokemon.json", 'r', encoding="utf-8") as file:
    pokemon_info = json.load(file)

print(json.dumps(pokemon_info, indent=4))