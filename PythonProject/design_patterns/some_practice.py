# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.

# from abc import ABC , abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("drawing a circle")

# class Triangle(Shape):
#     def draw(self):
#         print("drawing a Triangle")


# class ShapeFactory():
#     # @staticmethod
#     def create(self , shape : str) -> Shape:
#         if shape.lower() == 'circle':
#              return Circle()
#         else:
#             return Triangle()


# obj = ShapeFactory()
# print((obj.create("circle").draw()))

# print("Try programiz.pro")
'''
# -------singleton method!

class singleton:
    __instance = None
    def __new__(cls , *args , **kwargs):
        if cls.__instance is None:
            cls.__instance = "super().__new__(cls)"
        return cls.__instance

# __new__() controls object creation

obj1 = singleton()
obj2 = singleton()

print(obj1 is obj2)

class singleton1:
    __instance = None
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

obj11 = singleton1.get_instance()
obj22 = singleton1.get_instance()

print(obj11 is obj22)

#another method!!!

'''


#------observer_pattern-------
class bulb:
    def update(self , val , val1):
        print(f"power {val} and bulb is {val1}")

class fan:
    def update(self , val , val1):
        print(f"power {val} and fan is {val1}")


class oberver_patter:
    observers = [bulb()]
    @classmethod
    def new_state(cls , val , val1):
        for obs in cls.observers:
            obs.update(val , val1)

    @classmethod
    def add_observer(cls , obs):
        cls.observers.append(obs)

oberver_patter.add_observer(fan())
oberver_patter.add_observer(fan())
oberver_patter.add_observer(fan())
print(oberver_patter.new_state("came" , "on"))
print(oberver_patter.new_state("goes" , "off"))

# print("a")


# --- builder pattern ----


# ------strategy pattern------



