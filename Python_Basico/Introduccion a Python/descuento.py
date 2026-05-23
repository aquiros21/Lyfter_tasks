precio_producto = int(input("Ingrese precio de producto: "))

if precio_producto <= 100:
    descuento = precio_producto * 0.02

else:
    descuento = precio_producto * 0.10

precio_final = precio_producto - descuento

print(f"El precio final es de: {precio_final}")



