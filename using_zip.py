"""
for item1, item2, ... in zip(iterable1, iterable2, ...):
    # Code to execute for each pair of items
"""

def fun():
    list_1 = ['apple', 'banana', 'cherry']
    list_2 = [1, 2, 3]

    for fruit, number in zip(list_1, list_2):
        print(f"I have a {fruit} and its number is {number}.")



if __name__ == "__main__":
    fun()
