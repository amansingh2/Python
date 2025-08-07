# it hides internal details of a class and restrict direct access to its data. This ensures better data security and modularity.

'''
Python uses naming conventions to indicate access levels:
	•	Public (name) → Accessible from anywhere.
	•	Protected (_name) → Conventionally used as protected (still accessible but intended for internal use).
	•	Private (__name) → Name-mangled to prevent accidental access.
'''
class BankAccount:
    def __init__(self , owner , balance):
        self.owner = owner
        self._account_type = "Saving"
        self.__balance = balance
    def deposit(self , amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance;

acc = BankAccount("Aman" , 100)
print(acc.owner)
print(acc._account_type)
print(acc.get_balance())
acc.deposit(15)


#name Mangling(Accessing private Variables)! , Python mangles them with _ClassName__variableName.
print(acc._BankAccount__balance)

# we should use getter and setter for best practice!!!

class Person:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age
    def get_age(self):
        return self.__age;
    def set_age(self , new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            raise ValueError("Age must be greater than 0!")

p = Person("Amana" , 25)
print(p.get_age())
p.set_age(30)
print(p.get_age())



class Student:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age

    @property #act as a getter
    def age(self):
        return self.__age

    @age.setter  #Act as a setter
    def age(self , new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            self.__age  = 18

s = Student("Aman" , 33)
print(s.age)
s.age = 34
print(s.age)

#No need to call get_age() or set_age(), just use p.age.

class Car:
    def __init__(self, model, price):
        self.__model = model
        self.__price = price

    @property
    def price(self):
        return self.__price  # No setter → Read-only

c = Car("Tesla", 50000)
print(c.price)
# c.price = 60000  #  AttributeError: can't set attribute


