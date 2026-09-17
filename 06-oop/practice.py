# Day 6 OOP practice

# 1. Create a Rectangle class that calculates area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
print("Rectangle area:", rectangle.area())


# 2. Create a Person class with a method to introduce itself.
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)


person = Person("Student")
person.introduce()


# 3. Practice inheritance.
class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Bike(Vehicle):
    pass


bike = Bike()
bike.move()
