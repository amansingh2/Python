from dataclasses import dataclass
from dataclasses import field
"""
What is a dataclass?
A dataclass is a Python decorator (@dataclass) introduced in Python 3.7,
which automatically generates special methods like:
	•	__init__
	•	__repr__
	•	__eq__
	•	(and optionally __hash__, __lt__, etc.)
This saves boilerplate code when creating classes meant for storing data.
"""

#Normal Class!
class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"

# we have to manually write the __init__ and __repr__.


# With dataclasses!
@dataclass
class Person:
    name: str
    age: int
    city: str

"""
Done! Python automatically generates __init__, __repr__, and __eq__.
"""

# features of dataclasses!!
"""
1. Auto __init__
"""
p1 = Person("Alice", 25, "New York")
print(p1)
# Person(name='Alice', age=25, city='New York')

# 2. Equality Check!
p2 = Person("Alice", 25, "New York")
print(p1 == p2)  # True

# 3. Default values
@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"

p = Person("Bob", 30)
print(p)  # Person(name='Bob', age=30, city='Unknown')

# 4.field() for customization
@dataclass
class Person:
    name: str
    age: int
    city: str = field(default="Unknown", repr=False)  # hide in repr

p = Person("Charlie", 28)
print(p)  # Person(name='Charlie', age=28)

# 5.Frozen dataclass (immutable)
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 10  #  Error (frozen dataclass is immutable)

# 6. Ordering
@dataclass(order=True)
class Student:
    grade: int
    name: str

s1 = Student(90, "Alice")
s2 = Student(85, "Bob")
print(s1 > s2)  # True (because 90 > 85)

# 7. Convert to dictionary
from dataclasses import asdict

p = Person("Alice", 25, "Paris")
print(asdict(p))
# {'name': 'Alice', 'age': 25, 'city': 'Paris'}

"""
When to use dataclasses?
	•	When you just need a class for storing data (like DTOs, configs, records).
	•	Replaces boilerplate-heavy code.
	•	Great for cleaner, more maintainable code.
	
Summary:
	•	Use @dataclass for data-centric classes.
	•	Reduces boilerplate (__init__, __repr__, __eq__, etc.).
	•	Supports defaults, immutability, ordering, and easy conversions.

"""


if __name__ == "__main__":
    pass