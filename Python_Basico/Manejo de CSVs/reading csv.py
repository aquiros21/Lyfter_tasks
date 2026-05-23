import csv

def reading_csv(file_path):
    with open(file_path, 'r', encoding="utf-8") as file: 
        reader = csv.DictReader(file, delimiter='\t')

        for game in reader:
            print(dict(game))

reading_csv('new_videogames_info.tsv')