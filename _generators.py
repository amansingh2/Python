"""
Generators are a special type of iterator in Python that are created using a
function with the yield keyword instead of return. Unlike a normal function
that computes and returns all its results at once, a generator function yields
a single value at a time and then pauses its execution. When asked for the next
value, it resumes right where it left off, with its entire state (local variables,
instruction pointer, etc.) preserved.

This "on-demand" nature means they don't hold all values in memory simultaneously.
Instead, they produce values one by one as they're requested.
"""

"""
Why are They Used?
Generators are primarily used for their efficiency and elegant design, 
particularly in scenarios involving large amounts of data.

Memory Efficiency: This is the biggest reason to use generators. 
When you're dealing with massive datasets (e.g., a huge log file, 
a large CSV file, or a data stream), creating a list of all items 
can consume an unmanageable amount of memory and potentially crash 
your program. A generator, however, only ever holds one item in memory 
at a time. This makes them perfect for processing data that's too big to fit in RAM.

Lazy Evaluation: Generators compute values only when they are needed. 
This is known as lazy evaluation. This can significantly improve 
performance in cases where you might not need to process every single 
item in a sequence. For example, if you're searching for a specific 
value in a large dataset, a generator will stop producing values as 
soon as it finds the one you're looking for, saving valuable computation time.


-> Infinite Sequences: You can use yield to create generators for infinite 
sequences (e.g., an endless stream of Fibonacci numbers) without worrying 
about memory issues, as only a single value is ever stored at a time.
"""


def func():
    def simple_counter():
        print("Starting counter...")
        n = 1
        yield n

        print("Resuming...")
        n += 1
        yield n

        print("Finishing up...")
        n += 1
        yield n

    # Create the generator object
    my_counter = simple_counter()

    # Iterate over the generator
    print(next(my_counter))  # Output: Starting counter...
                             #         1
    print(next(my_counter))  # Output: Resuming...
                             #         2
    print(next(my_counter))  # Output: Finishing up...
                             #         3

    try:
        print(next(my_counter))
    except StopIteration:
        print("Generator exhausted.")

if __name__ == "__main__":
    func()