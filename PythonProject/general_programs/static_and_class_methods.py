#staticmethod -> Independent Utility ,
#A static method behaves like a regular function , but it's inside a class for logical grouping

class MathUtils:
    @staticmethod
    def add(a : int , b : int) -> int:  # no self or cls used here
        return a + b

print(MathUtils.add(34 , 31))

#No self or cls is required since it doesn’t depend on class or instance attributes.


#classmethod -> class Level method
#A @classmethod gets access to the class(cls) and can modify class attributes.

class Person:
    species = "Human"  # class attribtue

    @classmethod
    def change_species(cls , new_species):
        cls.species = new_species

print(Person.species)
Person.change_species("ABC")
print(Person.species)
