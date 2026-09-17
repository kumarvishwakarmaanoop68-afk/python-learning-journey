# Instance methods

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def double(self):
        return self.number * 2


calc = Calculator(5)

print("Square:", calc.square())
print("Double:", calc.double())
