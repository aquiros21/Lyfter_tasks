import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from actions import display_students, average_grades, top_3_students, failed_students
from data import asking_grade, asking_group, get_student, save_students, delete_student
from menu import show_menu

def menu_actions():
    while True:
        show_menu()
        option = input()

        if option == "1":
            student = get_student()
            save_students(student)
        elif option == "2":
            delete_student()
        elif option == "3":
            display_students("students.csv")
        elif option == "4":
            average_grades()
        elif option == "5":
            top_3_students()
        elif option == "6":
            failed_students()
        elif option == "7":
            print("Exiting the program")
            break
        else: print("Please enter only an option from 1 to 7")

menu_actions()

