numbers = []

while len(numbers) < 10:
    try:
        number = int(input(f"Ingrese un numero#{len(numbers) +1}: "))
        numbers.append(number)
    except ValueError:
        print("Porfavor ingrese solo numeros enteros")

print(numbers)
max = max(numbers)

print("El numero mas alto es:", max)

