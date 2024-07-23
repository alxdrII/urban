class Rect:
    def __init__(self, x, y, width, height):
        args = x, y, width, height
        if not (all(type(x) in (int, float) for x in args) and width > 0 and height > 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        raise TypeError('прямоугольники пересекаются')


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1)
]

lst_not_collision = []
for rect1 in lst_rect:
    try:
        for rect2 in lst_rect:
            if rect1 == rect2:
                continue

            rect1.is_collision(rect2)

    except TypeError:
        continue

    else:
        lst_not_collision.append(rect1)

print(lst_not_collision)

