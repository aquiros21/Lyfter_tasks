import json


def ask_number(prompt, convert=int):
    while True:
        try:
            return convert(input(prompt))
        except ValueError:
            print("Please enter only digits")


def ask_stat(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter only numbers from 0 to 100")
        except ValueError:
            print("Please enter only digits")


def get_pokemon_input():
    print("Please enter the following details for your pokemon:")
    name = input("Name: ")
    type_ = input("Type: ")
    level = ask_stat("Level: ")
    weight_kg = ask_number("Weight(kg): ", convert=float)
    is_shiny = input("Is it shiny? (yes/no): ").lower() == "yes"
    held_item = input("Enter held item or press enter when none: ") or None

    skills = []
    print("Please enter up to 4 skills (press enter when empty to stop):")
    while len(skills) < 4:
        skill = input(f"Skill {len(skills) + 1}: ")
        if skill == "":
            break
        skills.append(skill)

    print("For stats, please enter only numbers from 0 to 100:")
    stats = {
        "hp":         ask_stat("  HP: "),
        "attack":     ask_stat("  Attack: "),
        "defense":    ask_stat("  Defense: "),
        "sp_attack":  ask_stat("  Sp. Attack: "),
        "sp_defense": ask_stat("  Sp. Defense: "),
        "speed":      ask_stat("  Speed: ")
    }

    return {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }


def add_pokemon(new_pokemon):
    with open("pokemon.json", "r", encoding="utf-8") as file:
        pokemon_data = json.load(file)

    pokemon_data.append(new_pokemon)

    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(pokemon_data, file, indent=4)

    print(f"\n{new_pokemon['name']} was added successfully!")


def display_pokemon():
    with open("pokemon.json", "r", encoding="utf-8") as file:
        pokemon_data = json.load(file)

    print(json.dumps(pokemon_data, indent=4))


def main():
    new_pokemon = get_pokemon_input()
    add_pokemon(new_pokemon)
    display_pokemon()

