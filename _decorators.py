"""
A decorator in Python is just a function that takes another function (or class) as input,
adds some behavior, and returns it. It’s like “wrapping” a function with extra functionality.

You → Original Function → Decorator → Enhanced Function
"""

"""
Functions are first-class in Python
Since functions are objects, you can:
"""

def fun():
    def greet():
        return "Hello!"

    say_hello = greet   # assign function to variable
    print(say_hello())  # Hello!

"""
we can also pass functions as arguments and return them from other functions.
"""

# Decorator Example!

def func_deco():
    def decorator(func):
        def wrapper():
            print("Before the function runs")
            result = func()
            print("After the function runs")
            return result
        return wrapper

    @decorator
    def say_hello():
        print("Hello!")

    say_hello()

# Decorator with example!!
def func_deco_exa():
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Function is about to run...")
            result = func(*args, **kwargs)
            print("Function has run.")
            return result

        return wrapper

    @decorator
    def add(a, b):
        return a + b

    print(add(3, 5))


"""
Some built in decorators!!!Python already has some decorators:
@staticmethod
@classmethod
@property
@functools.lru_cache
"""

if __name__ == "__main__":
    func_deco_exa()