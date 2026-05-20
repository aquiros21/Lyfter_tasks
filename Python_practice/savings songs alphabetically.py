def reading_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def clean_and_sort(songs):
    cleaned = []
    for song in songs:
        song = song.strip()
        song = song.strip('"')
        cleaned.append(song)
    cleaned.sort()
    return cleaned


def create_file(path, songs):
    with open(path, "x", encoding= "utf-8") as file:
        for song in songs:
            file.write(song + "\n")


songs = reading_file("songs_list.txt")
sorted_songs = clean_and_sort(songs)
create_file("sorted_songs.txt", sorted_songs)


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        songs = file.read()
        print(songs)

read_file("sorted_songs.txt")
