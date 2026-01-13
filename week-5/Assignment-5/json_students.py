import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    grades = student["grades"]
    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)
    student["average"] = average

with open("students_result.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
