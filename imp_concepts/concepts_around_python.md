# What is `init` in python

- `__init__` is a special method (also called a magic method or dunder method, short for "double underscore") that gets called automatically when a new object of a class is created.
- It is used to initialize the attributes of the class.

`class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

```
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```
- When we create instance like below:
- `obj = MyClass('hello', 123)`
- What python does is:
  - creates an empty object of MyClass.
  - automatically call `__init__` on it with the provided arguments.

    
# Why is __init__ important?
- It allows each object to start with its own data.
- It binds parameters to object attributes using self.
- It's like a constructor, but not technically one (since Python doesn’t require constructors the way Java or C++ does).


# Some Key Points
- `self` refers to the instance being created. Must always be the first parameter.
- `Overridin` You can only have one __init__ per class, but can use *args/**kwargs for flexibility.
- If we don't define `__init__`, Python will use the default constructor.
 
# `__init__` vs `__new__`
- `__new__` actually creates the object (rarely overridden).
- `__init__` initializes it.

```
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self, x):
        print("Initializing with", x)
```
## Avoid!
- Forgetting self in the __init__ signature.


