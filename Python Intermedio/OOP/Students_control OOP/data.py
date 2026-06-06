import csv
import os

students_list = []


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

class Student():
    def __init__(self, name, group, spanish_grade, english_grade, science_grade, social_grade):
        self.name = name
        self.group = group
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade= science_grade
        self.social_grade = social_grade

def get_student():
    print("Please enter the following information for each student: ")
    full_name = input("Please enter student's full name: ")
    group = asking_group("Please enter student's group: ")
    spanish_grade = asking_grade("Please enter Spanish's grade: ")
    english_grade = asking_grade("Please enter English's grade: ")
    science_grade = asking_grade("Please enter science's grade: ")
    social_grade =  asking_grade("Please enter social studies grade: ")

    student = Student(full_name, group, spanish_grade, english_grade, science_grade, social_grade)

    students_list.append(student)
    print("Student(s) successfully added!")
    return student


def delete_student():
    name = input("Please enter the name of the student you want to delete: ").strip()
    group = input("Please enter the group of the student you want to delete: ").strip().upper()

    student_found = None
    for student in students_list:
        if student.name.lower() == name.lower() and student.group.upper() == group:
            student_found = student
            break
    
    if not student_found:
        print("Student not found, please double check entry.")
        return
    
    print(f"\nYou are about to delete: {student_found}")
    confirm = input("Are you sure? (Yes/No): ").strip().lower()

    if confirm == "yes":
        students_list.remove(student_found)
        print("Student successfully deleted!")
    else:
        print("Deletion canceled.")


def export_students():
    if not students_list:
        print("No students to export.")
        return

    existing_students = []
    file_exists = os.path.exists("students.csv")

    if file_exists:
        with open("students.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_students = list(reader)

    new_students = []
    for student in students_list:
        is_duplicate = any(
            e["full_name"].lower() == student.name.lower() and
            e["group"].upper() == student.group.upper()
            for e in existing_students
        )
        if not is_duplicate:
            new_students.append({
                "full_name": student.name,
                "group": student.group,
                "spanish_grade": student.spanish_grade,
                "english_grade": student.english_grade,
                "science_grade": student.science_grade,
                "social_grade": student.social_grade
            })

    if not new_students:
        print("No new students to export, all already exist in the CSV.")
        return

    with open("students.csv", "a", encoding="utf-8", newline="") as f:
        fieldnames = ["full_name", "group", "spanish_grade", "english_grade", "science_grade", "social_grade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(new_students)

    print(f"{len(new_students)} student(s) successfully exported to students.csv!")


def import_students():
    if not os.path.exists("students.csv"):
        print("No previously exported CSV file found.")
        return

    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        imported_students = list(reader)

    if not imported_students:
        print("The CSV file is empty.")
        return

    duplicates = 0
    added = 0

    for student in imported_students:
        student_obj = Student(
            student["full_name"],
            student["group"],
            student["spanish_grade"],
            student["english_grade"],
            student["science_grade"],
            student["social_grade"]
        )
        is_duplicate = any(
        e.name.lower() == student_obj.name.lower() and
        e.group.upper() == student_obj.group.upper()
        for e in students_list
        )
        if not is_duplicate:
            students_list.append(student_obj)
            added += 1
        else:
            duplicates += 1

    print(f"{added} student(s) successfully imported!")
    if duplicates > 0:
        print(f"{duplicates} student(s) skipped because they were already in the list.")



