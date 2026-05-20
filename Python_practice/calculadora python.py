def get_number(Prompt):
    while True:
        try:
            return float(input(Prompt))
        except ValueError as e:
            print(f"Error: Please enter a valid number: {e}")


def show_menu(current_number):
    print("Please select an option from the menu below:")
    print(f"Current number: {current_number}")
    print(f'1. Addition')
    print(f'2. Subtraction')
    print(f'3. Multiplication')
    print(f'4. Division')
    print(f'5. Clear Result')
    print(f'6. Exit')


def calculator():
    current_number = 0

    while True:
        show_menu(current_number)

        option = input()

        if option == "1":
            num = get_number("Please enter a number to add: ")
            current_number += num
        elif option == "2":
            num = get_number("Please enter a number to subtract: ")
            current_number -= num
        elif option == "3":
            num = get_number("Please enter a number to multiply: ")
            current_number *= num
        elif option == "4":
            num = get_number("Please enter a number to divide: ")
            try:
                current_number /= num
            except ZeroDivisionError as e:
                print(f'Please enter a valid number to divide, Error: {e}')
        elif option == "5":
            current_number = 0
            print("Result cleared")
        elif option == "6":
            print("Exiting now")
            break
        else:
            print("Please enter only from options 1 to 6")

    print (f"Final Result is: {current_number}")

calculator()
