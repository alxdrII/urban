from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__color = []  # (список цветов в формате RGB)
        self.__sides = []  # (список сторон(целые числа))
        self.filled = True # закрашенный

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        pass

    def set_color(self, r, g, b):
        pass

    def __is_valid_sides(self, *args):
        pass

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circum):
        super().__init__()
        self.__radius = circum / 2 / pi

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side):
        super().__init__()
        self.__height = 0


class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, side):
        super().__init__(color)
        self.__sides = [side for _ in range(12)]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())