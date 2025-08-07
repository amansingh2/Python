'''
What is the Factory Pattern?
	•	The Factory Pattern is a creational design pattern that provides a way to create objects without specifying the exact class that will be instantiated.
	•	It encapsulates object creation in a separate method (factory method).
	•	It is useful when the exact type of object to be created depends on input conditions.
'''

'''
Let’s create a shape factory that returns different shapes (Circle, Rectangle) without exposing the exact instantiation logic.
'''

from abc import ABC, abstractmethod

# Step 1: Define an abstract class (Interface)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Concrete Implementations
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Step 3: Factory Method to Create Objects
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Unknown shape type")

# ✅ Example Usage
shape1 = ShapeFactory.get_shape("circle")
print(shape1.draw())  # ✅ Output: Drawing a Circle

shape2 = ShapeFactory.get_shape("rectangle")
print(shape2.draw())  # ✅ Output: Drawing a Rectangle


'''
🔥 When to Use Factory Pattern?

✔️ When you want to encapsulate object creation.
✔️ When the exact type of object is determined at runtime.
✔️ When you want to avoid tight coupling between object creation and usage.

'''