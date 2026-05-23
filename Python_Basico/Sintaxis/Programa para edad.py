name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad "))

if age  <= 3:
    category = "Bebe"
elif age <= 8:
    category = "Nino"
elif age <= 12:
    category = "Preadolecente" 
elif age <= 16: 
    category = "Adolecente"
elif age <= 30:
    category = "Adulto Joven" 
elif age <= 50:
    category = "Adulto" \

else:
    category = "Adulto mayor" 

print(f"{name}, usted es considerado una persona {category}")
