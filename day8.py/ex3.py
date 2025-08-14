# Base class
class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email  # private

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")

    def get_email(self):
        return self.__email


# Subclass: Student
class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}")
        else:
            print(f"{self.name} is already enrolled in {course}")

    # Magic methods
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', gpa={self.gpa})"


# Subclass: Professor
class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = []

    def add_course(self, course):
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            print(f"{self.name} is now teaching {course}")
        else:
            print(f"{self.name} is already teaching {course}")

    def __repr__(self):
        return f"Professor(id={self.id}, name='{self.name}', dept='{self.department}')"



if __name__ == "__main__":
    s1 = Student(1, "saifalnimer", "saif@example.com", "Computer Science", 3.9)
    s2 = Student(2, "hmz", "hmz@example.com", "Mathematics", 3.5)

    p1 = Professor(101, "Dr. nasser", "nasser@example.com", "Computer Science")

    s1.enroll("Algorithms")
    s2.enroll("Calculus")

    p1.add_course("Algorithms")
    p1.add_course("AI")

    s1.display_info()
    p1.display_info()

    print(s1 < s2)  

    print(repr(s1))
    print(repr(p1))
