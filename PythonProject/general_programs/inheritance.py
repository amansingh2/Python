class Animal:
    def speak(self):
        return "Animal makes sound"

class Dog(Animal):
    def barks(self):  # we can Override it as well!!
        return "Dog Barks"

# print(Dog().speak())
# print(Animal().speak())

class Cat(Animal):
    def speak(self):
        return super().speak() + " but Cat meowss"

print(Cat().speak())

class Fly:
    def fly(self):
        return "I can Fly!"
class Swim:
    def swim(self):
        return "I Can Swim"

class Duck(Fly , Swim):
    pass    # Placeholder for future code or # Empty class definition

duck = Duck()
print((Duck()).swim() +" " + duck.fly())





