def sort_alphabetic(string):
    words_list = string.split("-")
    words_list.sort()
    return "-".join(words_list)


if __name__ == '__main__':
    print(sort_alphabetic("apple-house-car-berries"))
