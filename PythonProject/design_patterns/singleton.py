# -------singleton method!

class singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
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