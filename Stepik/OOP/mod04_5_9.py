class PointTrack:
    """Хранит коортинату точки"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')

        super().__setattr__(key, value)

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


class Track:
    """класс для представления маршрутов в навигаторе"""



p = PointTrack(4, 5.5)
print(p)
