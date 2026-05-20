def sort_alphabetic(string):
    list = string.split("-")
    list.sort()
    return "-".join(list)


print(sort_alphabetic("apple-house-car-berries"))
