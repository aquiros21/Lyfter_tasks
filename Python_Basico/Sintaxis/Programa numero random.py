import random

answer = random.randint(1, 10)

while True:
    try:
        number = int(input("Ingrese un numero del 1 al 10: "))

        if number < 1 or number > 10:
            print("El numero debe ser del 1 al 10")
            continue

        if number < answer:
            print("El numero es mas alto")
        elif number > answer:
            print("El numero es menor")
        else:
            print("Felicidades")
            break

    except ValueError:
        print("Ingrese solo numeros del 1 al 10")
