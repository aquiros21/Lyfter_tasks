global_sample = "This is a Test For Upper case"

def count_capitals(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    print(f"There are {upper} case letters and there are {lower} lower case letters")

count_capitals(global_sample)
