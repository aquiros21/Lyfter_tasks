import csv
from actions import average_grades, top_3_students, failed_students
from data import asking_grade, asking_group, get_student, delete_student, export_students, import_students, students_list
from menu import show_menu


def menu_actions():
    while True:
        show_menu()
        option = input()

        if option == "1":
            get_student()
        elif option == "2":
            print(students_list)
            delete_student()
        elif option == "3":
            print(students_list)
        elif option == "4":
            average_grades()
        elif option == "5":
            top_3_students()
        elif option == "6":
            failed_students()
        elif option == "7":
            export_students()
        elif option == "8":
            import_students()
        elif option == "9":
            print("Exiting the program")
            break
        else: print("Please enter only an option from 1 to 9")

menu_actions()

