try:
    total_grades = int(input("Ingrese la cantidad de notas: "))

    grade_counter = 1
    passing_grades_count = 0
    failing_grades_count = 0
    passing_grades_sum = 0
    failing_grades_sum = 0
    total_grade_average = 0

    while grade_counter <= total_grades:
        current_grade = float(input(f"Ingrese la nota número {grade_counter}: "))

        if current_grade < 70:
            failing_grades_count += 1
            failing_grades_sum += current_grade
        else:
            passing_grades_count += 1
            passing_grades_sum += current_grade

        total_grade_average += current_grade / total_grades
        grade_counter += 1

    if passing_grades_count > 0:
        passing_grades_average = passing_grades_sum / passing_grades_count
    else:
        passing_grades_average = 0

    if failing_grades_count > 0:
        failing_grades_average = failing_grades_sum / failing_grades_count
    else:
        failing_grades_average = 0

    print("El estudiante tiene esta cantidad de notas aprobadas:", passing_grades_count)
    print("Este es el promedio de notas aprobadas:", passing_grades_average)

    print("El estudiante tiene esta cantidad de notas desaprobadas:", failing_grades_count)
    print("Este es el promedio de notas desaprobadas:", failing_grades_average)

    print("Este es el promedio total de notas:", total_grade_average)

except ValueError:
    print("Por favor ingrese valores numéricos válidos.")