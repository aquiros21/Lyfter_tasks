import csv
from data import students_list


def average_grades():
    if not students_list:
        print("No students found.")
        return

    total = 0
    count = 0

    for student in students_list:
        student_avg = (int(student.spanish_grade) + int(student.english_grade) + 
                        int(student.science_grade) + int(student.social_grade)) / 4
        total += student_avg
        count += 1

    overall_average = total / count
    print(f"Overall average of all students: {overall_average:.2f}")


def top_3_students():
    if not students_list:
        print("No students found.")
        return

    sorted_students = sorted(students_list, 
                            key=lambda s: (int(s.spanish_grade) + int(s.english_grade) + 
                                            int(s.science_grade) + int(s.social_grade)) / 4, 
                            reverse=True)

    top_3 = sorted_students[:3]

    print("\nTop 3 students with highest averages are:")
    for i, student in enumerate(top_3, start=1):
        avg = (int(student.spanish_grade) + int(student.english_grade) + 
            int(student.science_grade) + int(student.social_grade)) / 4
        print(f"{i}. {student.name} - Group: {student.group} - Average: {avg:.2f}")


def failed_students():
    if not students_list:
        print("No students found.")
        return

    subjects = {
        "spanish_grade": "Spanish",
        "english_grade": "English",
        "science_grade": "Science",
        "social_grade": "Social Studies"
    }

    found_failed = False

    for student in students_list:
        failed_subjects = []
        for key, subject_name in subjects.items():
            if int(getattr(student, key)) < 60:
                failed_subjects.append(f"{subject_name}: {getattr(student, key)}")

        if failed_subjects:
            found_failed = True
            print(f"\nStudent: {student.name} - Group: {student.group}")
            for subject in failed_subjects:
                print(f"   - {subject}")

    if not found_failed:
        print("No students with failed grades.")


