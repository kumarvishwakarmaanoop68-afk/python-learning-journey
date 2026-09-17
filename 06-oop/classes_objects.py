# Classes and objects

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Anoop", "Diploma IT")

print("Name:", student1.name)
print("Course:", student1.course)
