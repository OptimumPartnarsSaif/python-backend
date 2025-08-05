students = [
    ("Alice", 20, 88),
    ("Bob", 22, 75),
    ("Charlie", 19, 95),
    ("Diana", 21, 64),
    ("Ethan", 20, 79),
    ("Fay", 22, 91),
]

# 1. Sort by grade (descending)
sorted_by_grade = sorted(students, key=lambda student: student[2], reverse=True)
print("Sorted by grade (desc):", sorted_by_grade)

# 2. Filter: grades >= 80
passed_students = list(filter(lambda student: student[2] >= 80, students))
print("Students who passed:", passed_students)

# 3. Create "Name (Grade)" strings
name_grade_list = [f"{name} ({grade})" for name, _, grade in students]
print("Name and grades:", name_grade_list)

# 4. Average grade
average_grade = sum(student[2] for student in students) / len(students)
print("Average grade:", average_grade)
