list_a = ['first_name', 'last_name', 'gender', 'age']
list_b = ['Alek', 'Castillo', 'male', 26]

result = {}
for i in range(len(list_a)):
    result[list_a[i]] = list_b[i]
print(result)