"""
in-built functions
module functions : when we keep related functions and files then it is called module
user-defined functions : jinko hum khud banate hai
"""

"""
import math
print(dir(math)) #directory of maths , it'll tell about all functions of the maths
"""

# from math import sqrt
from math import * # star ka matlab sabhi import ho rhe hai
#it will import only sqrt function from math module

print(sqrt(4))
print(sqrt(10))

def print_sum(first , second=100):
    print(first + second)
print_sum(12 )

'''
User Defined functions
def function_name(parameters):
    do something
'''