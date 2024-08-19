import inspect
from pprint import pprint
from random import choice


class Cat:
    def __init__(self, name, age, weight, owner):
        self.name = name
        self.age = age
        self.weight = weight
        self.owner = owner
        self.__alive = True

    def it_s_birthday(self):
        self.age += 1
        return f'Happy birthday, {self.name}!!!'

    @property
    def alive(self):
        return self.__alive

    def it_s_died(self):
        if self.owner == 'Schrodinger':
            self.__alive = choice([True, False])
            return "Don't worry, maybe your cat is alive!"
        else:
            self.__alive = False
            return "We're sorry ;-("

    def __str__(self):
        return self.name


def introspection_info(obj):

    info = {}
    info['name'] = getattr(obj, "__name__", None)
    info['module'] = getattr(obj, "__module__", None)
    info['type'] = type(obj)
    info['functions'] = [x[0] for x in inspect.getmembers(obj, inspect.isfunction)]
    info['methods'] = [x[0] for x in inspect.getmembers(obj, inspect.ismethod)]

    return info


cat_tom = Cat("Tom", 5, 24, 'Free')

print(introspection_info(Cat))
print(introspection_info(cat_tom))
print(introspection_info(cat_tom.name))