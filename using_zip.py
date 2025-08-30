"""
for item1, item2, ... in zip(iterable1, iterable2, ...):
    # Code to execute for each pair of items
"""

def fun():
    list_1 = ['apple', 'banana', 'cherry']
    list_2 = [1, 2, 3]

    for fruit, number in zip(list_1, list_2):
        print(f"I have a {fruit} and its number is {number}.")


"""
zip() stops iterating when the shortest iterable is exhausted. 
Any remaining elements in the longer iterables are ignored.
"""
def fun2():
    names = ['Alice', 'Bob', 'Charlie', 'David']
    ages = [25, 30, 35]  # This list is shorter

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")

"""
You can use zip() with more than two iterables. 
The principle remains the same: it pairs up elements from all of them at each index.
"""

def fun3():
    names = ['Alice', 'Bob']
    ages = [25, 30]
    cities = ['New York', 'London']

    for name, age, city in zip(names, ages, cities):
        print(f"{name} is {age} and lives in {city}.")


"""
The * operator can be used with zip() to "unzip" a list of tuples back into separate lists.
"""

def fun4():
    packed_list = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    names, ages = zip(*packed_list)

    print(f"Names: {list(names)}")
    print(f"Ages: {list(ages)}")

if __name__ == "__main__":
    fun4()
