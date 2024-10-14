"""
Jørgen Asmundvaag
jorgen.asmundvaag@nmbu.no

Ivar Eftedal
ivar.odegardstuen.eftedal@nmbu.no
"""


class Person:
    def __init__(self, name: str, age: int, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_details(self):
        print(f"Name: {self.name:<15} Age: {self.age:<5} Email: {self.email:<10}")


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        email: str,
        student_id: int,
        courses=None,
        grades=None,
    ):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll_in_course(self, course: str):
        self.courses.append(course)

    def assign_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def get_grades(self):
        for key, values in self.grades.items():
            print(f"{self.name} has got the following grades: ")
            print(f"Subject: {key}, Grades: {values}")


class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, subject: str):
        super().__init__(name, age, email)
        self.subject = subject

    def assign_grade(self, student, grade):
        print(f"{student.name} assigned the grade: {grade}!")
        student.assign_grade(self.subject, grade)


class Course:
    def __init__(self, course_name: str, course_code: int, enrolled_students=[]):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = enrolled_students

    def add_student(self, student):
        self.enrolled_students.append(student)
        student.enroll_in_course(self.course_name)

    def list_students(self):
        print(f"Students enrolled in {self.course_name}: ")
        for student in self.enrolled_students:
            student.get_details()


ivar = Student("Ivar", 20, "ivar.eftedal@icloud.com", 1)
jorgen = Student("Jørgen", 19, "jorgen@icloud.com", 3)
christopher = Student("Christopher", 20, "christopher@icloud.com", 2)
ludvik = Student("Ludvik", 21, "ludvik@icloud.com", 4)
sebastian = Student("Sebastian", 25, "sebastian@icloud.com", 5)

john = Teacher("John", 40, "john.johnsen@gmail.com", "Math")
habib = Teacher("Habib", 45, "habib@gmail.com", "IT")
ola = Teacher("Ola", 60, "ola@gmail.com", "English")

ivar.get_details()
jorgen.get_details()
christopher.get_details()
ludvik.get_details()
sebastian.get_details()
print()

john.get_details()
habib.get_details()
ola.get_details()
print()

english = Course("English", 3)
english.add_student(ivar)
english.add_student(jorgen)
english.add_student(christopher)
print()

ola.assign_grade(ivar, 6)
ola.assign_grade(jorgen, 6)
ola.assign_grade(ivar, 2)
ola.assign_grade(jorgen, 5)
print()

ivar.get_grades()
jorgen.get_grades()
print()

english.list_students()
print()
