numbers = print("Ingrese 3 numeros distintos")

try:
    n1 = int(input("Ingrese el primer numero "))
    n2 = int(input("Ingrese el segundo numero "))
    n3 = int(input("ingrese el tercer numero "))

    print(f"El numero mayor es: {max(n1, n2, n3)}")

except ValueError:
    print("Digite solo numeros")

