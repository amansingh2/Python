class Dog:
    def __init__(self, name, breed):
        self.name = name        # setting instance variable 'name'
        self.breed = breed      # setting instance variable 'breed'

d = Dog("Buddy", "Labrador")

"""
What Happens:
Call Dog.__init__(d, "Buddy", "Labrador")
Set d.name = "Buddy"
Set d.breed = "Labrador"
"""

class Car:
    def __init__(self, brand="Toyota", year=2020):
        self.brand = brand
        self.year = year

c = Car()
print(c.brand)  # Toyota
print(c.year)   # 2020



class Example:
    def __init__(self, *args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
        
e = Example(1, 2, name="test", value=42)


