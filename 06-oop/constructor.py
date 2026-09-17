# Constructor using __init__

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car("Toyota", "Corolla")

print("Brand:", car.brand)
print("Model:", car.model)
