# Polymorphism

class Cat:
    def sound(self):
        print("Meow")


class Dog:
    def sound(self):
        print("Bark")


animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()
