class Car:
    def __init__(self):
        self.brand = None
        self.engine = None
        self.color = None

    def __str__(self):
        return f"Car(Brand: {self.brand}, Engine: {self.engine}, Color: {self.color})"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self  # Returning self allows method chaining

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car  # Returns the final object

# ✅ Example Usage
car = CarBuilder().set_brand("Tesla").set_engine("Electric").set_color("Red").build()
car1 = CarBuilder().set_brand("Tesla").set_engine("Electric").build()

print(car)  # ✅ Output: Car(Brand: Tesla, Engine: Electric, Color: Red)
print(car1)