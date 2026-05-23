def count_characters(string, character):
    total_count = 0
    for letter in string:
        if letter == character:
            total_count +=1
    return(total_count)


phrase = input("Por favor Ingrese la frase que quiera: ")
character = input("Por favor Ingrese cual letra quiere: ")

print(f"El numero total de sus letras es de: {count_characters(phrase,character)}")
