class Vector:
    def _check_coords(self, coords):
        for coord in coords:
            if not isinstance(coord, (int, float)):
                raise ValueError('координаты должны быть числами')

    def __init__(self, *coords):
        self._check_coords(coords)
        self.__coords = coords

    def __add__(self, other):
        v1 = self.get_coords()
        v2 = other.get_coords()
        if len(v1) != len(v2):
            raise TypeError('размерности векторов не совпадают')

        vn = tuple()
        for i in range(len(v1)):
            vn += (v1[i] + v2[i],)

        return type(self)(*vn)

    def __sub__(self, other):
        v1 = self.get_coords()
        v2 = other.get_coords()
        if len(v1) != len(v2):
            raise TypeError('размерности векторов не совпадают')

        vn = tuple()
        for i in range(len(v1)):
            vn += (v1[i] - v2[i],)

        return type(self)(*vn)

    def get_coords(self):
        return self.__coords


class VectorInt(Vector):
    def _check_coords(self, coords):
        for coord in coords:
            if not isinstance(coord, int):
                raise ValueError('координаты должны быть целыми числами')



v1 = VectorInt(1, 2, 3)
v2 = VectorInt(4, 5, 6)
v3 = v2 - v1
print(v3.get_coords(), type(v3))
