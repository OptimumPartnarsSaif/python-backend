school_name = "Python High"

def init(self, name):
        self.name = name
        self.grades = []

def add_grade(self, score):
        """Adds a grade to the list if it's between 0 and 100."""
        if 0 <= score <= 100:
            self.grades.append(score)
            print(f"Grade {score} added successfully.")
        else:
            print("Invalid grade. Please enter a score between 0 and 100.")

def average_grade(self):
        """Calculates the average of the student's grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

def student_info(self):
        """Returns a string with student details and average grade."""
        average = self.average_grade()
        return f"Name: {self.name}\nSchool: {self.school_name}\nAverage Grade: {average:.2f}"


print("\n--- Exercise 6: Student Grade Tracker with User Input ---")
student_name = input("Enter the student's name: ")
student = Student(student_name)

    while True:
        try:
        score_input = input("Enter a grade (or 'done' to finish): ")
        if score_input.lower() == 'done':
            break
        score = float(score_input)
        student.add_grade(score)
        except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

print(f"\n{student.student_info()}")
print("-" * 25)
