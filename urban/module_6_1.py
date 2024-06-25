class Plant:
    """ Растение """

    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible  # съедобность


class Flower(Plant):
    """ Цветок """
    pass


class Fruit(Plant):
    """ Фрукт """
    
    def __init__(self, name, edible=True):
        super().__init__(name, edible)


class Animal:
    """ Животное """

    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive  # живой
        self.fed = fed  # накормленный

    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True

        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    """ Млекопитающий """
    pass


class Predator(Animal):
    """ Хищник """
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
