import csv

def write_games_info (file_path, data):
    with open (file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


videogames_info = [
    {
        "Name": "COD",
        "Genre": "FPS",
        "Developer": "Activision",
        "ESRB Class": "T"
    },
    {
        "Name": "Fortnite",
        "Genre": "Battle Royale",
        "Developer": "Epic Games",
        "ESRB Class": "M"
    },
    {
        "Name": "Valorant",
        "Genre": "FPS",
        "Developer": "Riot Games",
        "ESRB Class": "R"
    },
    {
        "Name": "Rocket League",
        "Genre": "Sports",
        "Developer": "Psyonix",
        "ESRB Class": "M"
    }
]

write_games_info('new_videogames_info.tsv', videogames_info)