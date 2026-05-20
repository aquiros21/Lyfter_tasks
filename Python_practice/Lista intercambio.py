list = ["Quiros", "Vargas", "Rodriguez", "Solano", "Mendez"]

if len(list) > 1:
    list[0], list[-1] = list[-1], list[0]

print(list)