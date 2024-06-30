from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if not self.__is_valid_color(color):
            raise ValueError('Неверные параметры цвета')

        self.__color = color  # (список цветов в формате RGB)

        if self.__is_valid_sides(sides):
            self.__sides = sides  # (список сторон(целые числа))
        else:
            self.__sides = tuple(1 for _ in range(self.sides_count))

        self.filled = True  # закрашенный

    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(color):
        return isinstance(color, tuple) and len(color) == 3 and all(isinstance(x, int) and 0 <= x <= 255 for x in color)

    def set_color(self, r, g, b):
        color = r, g, b
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, sides):
        return len(sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / 2 / pi

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if not self.is_triangle(sides):
            raise ValueError('Стороны не являются треугольником!')

        self.__height = self.height_triangle(sides[2])

    @staticmethod
    def is_triangle(sides):
        a, b, c = sides
        return a + b > c and a + c > b and b + c > a

    def set_sides(self, *sides):
        super().set_sides(*sides)
        if not self.is_triangle(sides):
            raise ValueError('Фигура не является треугольником!')

    def get_square(self):
        """
        Вычисляем площадь по формуле Герона: S = √(р (р — а)(р — b)(p — c)),
        где a, b и с — значения длин сторон, р — половина периметра.

        """
        p = len(self) / 2
        sides = self.get_sides()
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

    def height_triangle(self, base: int):
        """Вычисляем высоту через площадь и длинну стророны треугольника"""

        if base in self.get_sides():
            return 2 * self.get_square() / base
        else:
            raise ValueError('Значение не является базой треугольника')


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0] for _ in range(12)]

        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
trang1 = Triangle((10, 55, 255), 5, 8, 9)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка сторон и площади треугольника
print(trang1.get_sides())
print(trang1.get_square())
trang1.set_sides(1, 10, 1)  # Ошибка: фигура не треугольник
