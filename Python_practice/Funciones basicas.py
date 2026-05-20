global_sum = 25 + 30 + 10
global_name = "Adrian"


def sum_two_numbers (num_1 , num_2=10):
    return(num_1 + num_2)


def add_pctg_sign (result):
    return f"{result}%"


def change_name():
    global global_name
    global_name = "Andres"


def sum_and_add_pctg(num_1, num_2):
    result = sum_two_numbers(num_1, num_2)
    return add_pctg_sign(result)


print(add_pctg_sign(global_sum))

print(sum_two_numbers(5 , 25))

print(add_pctg_sign(sum_two_numbers(10)))

change_name()
print(global_name)

print(sum_and_add_pctg(10, 20)) 




