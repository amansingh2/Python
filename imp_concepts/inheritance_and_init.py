class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent __init__
        self.color = color
