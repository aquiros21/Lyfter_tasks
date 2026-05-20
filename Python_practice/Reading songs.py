def reading_file(path):
    with open(path, "r", encoding= "utf-8") as file:
        songs = file.read()
        print(songs)


reading_file("songs_list.txt")




