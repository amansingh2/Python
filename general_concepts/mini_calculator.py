first = input("enter first number : ")
operator = input("enter operator (+ , - , * , / , %) : ")
second = input("enter second number : ")

if operator == '+':
    print(int(first) + int(second))
elif operator == '-':
    print(int(first) - int(second))
elif operator == '*':
    print(int(first) * int(second))
elif operator == '/':
    print(int(first) / int(second))
else:
    print(int(first) % int(second))

