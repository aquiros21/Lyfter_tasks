def count_characters(string, character):
    total_count = 0
    for letter in string:
        if letter == character:
            total_count +=1
    return(total_count)


phrase = input("Ingrese la frase que quiera: ")
character = input("Ingrese cual letra quiere: ")

print(f"El numero total de sus letras es de: {count_characters(phrase,character)}")
