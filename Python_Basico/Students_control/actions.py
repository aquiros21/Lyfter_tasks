import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def display_students(filename):
    with open(filename, "r", encoding="utf-8") as f:
        display_list = csv.DictReader(f)
        for student in display_list:
            print(dict(student))


def average_grades():
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    if not students:
        print("No students found.")
        return

    total = 0
    count = 0

    for student in students:
        student_avg = (int(student["spanish_grade"]) + int(student["english_grade"]) + 
                        int(student["science_grade"]) + int(student["social_grade"])) / 4
        total += student_avg
        count += 1

    overall_average = total / count
    print(f"Overall average of all students: {overall_average:.2f}")


def top_3_students():
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    if not students:
        print("No students found.")
        return

    for student in students:
        student["average"] = (int(student["spanish_grade"]) + int(student["english_grade"]) +
                            int(student["science_grade"]) + int(student["social_grade"])) / 4

    sorted_students = sorted(students, key=lambda s: s["average"], reverse=True)

    top_3 = sorted_students[:3]

    print("\nTop 3 students with highest averages are:")
    for i, student in enumerate(top_3, start=1):
        print(f"{i}. {student['full_name']} - Group: {student['group']} - Average: {student['average']:.2f}")


def failed_students():
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    if not students:
        print("No students found.")
        return

    subjects = {
        "spanish_grade": "Spanish",
        "english_grade": "English",
        "science_grade": "Science",
        "social_grade": "Social Studies"
    }

    found_failed = False

    for student in students:
        failed_subjects = []
        for key, subject_name in subjects.items():
            if int(student[key]) < 60:
                failed_subjects.append(f"{subject_name}: {student[key]}")

        if failed_subjects:
            found_failed = True
            print(f"\nStudent: {student['full_name']} - Group: {student['group']}")
            for subject in failed_subjects:
                print(f"   - {subject}")

    if not found_failed:
        print("No students with failed grades.")