import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    print("Student added.")

def get_all_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    if students:
        print("\n--- All Students ---")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        print("--------------------")
    else:
        print("No students found.")

def update_student_grade(student_id, new_grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
    print("Student grade updated.")

def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted.")

def main():
    init_db()
    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            get_all_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            new_grade = input("Enter new grade: ")
            update_student_grade(student_id, new_grade)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()