from collections import deque
from tkinter.font import names


def add_two(*args):   #iska data_type tuple hota hai
    print(args)
    return sum(args)


def printing(**kwargs):  #iska data_type dictionary hota hai
    print(kwargs)

print(add_two(1 , 2 , 3 , 6))

print(printing(name = "Aman" , age = 12 , score = 100))

arr = [1 , 2 , 4] # list hai array ni hai!
arr.append(12)
arr.append(34)
print(arr)

x = sum([i if i % 2 == 0 else 5 for i in range(0 , 5)]) #ternary operator
print(x)

y = {a : a*a for a in range(5)}

print(y)

dict = {}

