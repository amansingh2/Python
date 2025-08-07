def number_generator(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

# Using yield to create a generator
my_generator = number_generator(3)

# Using next() to iterate through the generator
print(next(my_generator))  # Output: 0
print(next(my_generator))  # Output: 1
print(next(my_generator))  # Output: 2

print(next(my_generator))  # Raises StopIteration