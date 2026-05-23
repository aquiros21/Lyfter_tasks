list_of_keys = ['last_name', 'role']
user = {'name': 'Adrian', 'last_name': 'Quiros', 'email': 'adrian@gmail', 'role': 'engineer', 'age': 35}

for key in list_of_keys:
    user.pop(key, None)

print(user)