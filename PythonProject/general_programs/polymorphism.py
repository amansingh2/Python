#Polymorphism allows one interface to be used for different data types or classes, making code more flexible and reusable.
#method - overriding
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Barks"

class Cat(Animal):
    def speak(self):
        return "Meows"

animals = [Dog() , Cat()]
#Different classes have the same method (speak()), but behavior changes
for animal in animals:
    print(animal.speak())

#Function Over-loading

print(len("Aman Singh"))         #string length
print(len([1 , 2 , 3 , 4]))      #array length
print(len({"a" : 1 , "b" : 2}))  # dict length

#operator overloading in python

print(5 + 10)
print("Hello" + " World!")
print([1 , 2] + [3 , 4])

#implementing operator overloading in class!!!

class Book:
    def __init__(self , pages):
        self.pages = pages
    def __add__(self , other):
        return Book(self.pages + other.pages)
    def __str__(self):
        return f"Total pages : {self.pages} "

book1 = Book(100)
book2 = Book(200)
combined = book1 + book2

print(combined)
