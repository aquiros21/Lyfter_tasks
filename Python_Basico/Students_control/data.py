import csv
import os
from actions import display_students
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def asking_grade(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter only numbers from 0 to 100")
        except ValueError:
                print("Please enter digits only")


def asking_group(prompt):
    valid_letters = ["A", "B", "C"]
    while True:
        value = input(prompt).strip().upper()
        if len(value) >= 2:
            number_part = value[:-1]   
            letter_part = value[-1]    
            if number_part.isdigit() and 1 <= int(number_part) <= 12 and letter_part in valid_letters:
                return value
        print("Invalid format. Please enter a number from 1-12 followed by A, B, or C (e.g. 11A, 10B)")


def get_student():
    print("Please enter the following information for each student: ")
    full_name = input("Please enter student's full name: ")
    group = asking_group("Please enter student's group: ")
    spanish_grade = asking_grade("Please enter Spanish's grade: ")
    english_grade = asking_grade("Please enter English's grade: ")
    science_grade = asking_grade("Please enter science's grade: ")
    social_grade =  asking_grade("Please enter social studies grade: ")

    student = {
        "full_name": full_name,
        "group": group,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "science_grade": science_grade,
        "social_grade": social_grade
    }
    students_list.append(student)
    print("Student(s) successfully added!")
    return student

students_list = []


def save_students(student):
    file_exists = os.path.exists("students.csv")
    
    with open("students.csv", "a", encoding="utf-8", newline="") as f:
        fieldnames = ["full_name", "group", "spanish_grade", "english_grade", "science_grade", "social_grade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()  
        
        writer.writerow(student)


def delete_student():
    display_students("students.csv")
    
    name = input("Enter the full name of the student you want to delete: ").strip()
    group = input("Enter the group of the student you want to delete: ").strip().upper()

    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    student_found = None
    for student in students:
        if student["full_name"].lower() == name.lower() and student["group"].upper() == group:
            student_found = student
            break

    if not student_found:
        print("Student not found, please check the name and group.")
        return

    print(f"\nYou are about to delete: {student_found}")
    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm == "yes":
        students.remove(student_found)
        with open("students.csv", "w", encoding="utf-8", newline="") as f:
            fieldnames = ["full_name", "group", "spanish_grade", "english_grade", "science_grade", "social_grade"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print("Student successfully deleted!")
    else:
        print("Deletion cancelled.")
