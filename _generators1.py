def func():
    # List comprehension (creates and stores all values in memory)
    list_of_squares = [x**2 for x in range(5)]
    print(list_of_squares)  # Output: [0, 1, 4, 9, 16]

    # Generator expression (creates values on-demand)
    gen_of_squares = (x**2 for x in range(5))

    # Iterate over the generator
    print(next(gen_of_squares))  # Output: 0
    print(next(gen_of_squares))  # Output: 1

    # Or use a for loop, which is the most common way to consume a generator
    for square in gen_of_squares:
        print(square)

if __name__ == "__main__":
    func()


