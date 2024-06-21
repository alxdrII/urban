class Cell:
    """ Клетка может содержать любые целые числа.

    Если содержимое клетки == 0 | "" | Folse..., то она считается свободной: is_free == True

    """
    def __init__(self, value=0):
        self.is_free = not bool(value)
        self.value = value

    def __bool__(self):
        return self.is_free

    def __setattr__(self, key, value):
        if key == "value":
            self.is_free = not bool(value)
            object.__setattr__(self, key, value)

    def __repr__(self):
        return str(self.value)


class TicTacToe:
    CROSS = 1
    ZERO = 2

    def __init__(self):
        self.pole = None
        self.clear()

    def __getitem__(self, item):
        if isinstance(item[0], slice):
            print(item[0])

        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if not (value in (self.CROSS, self.ZERO)):
            raise ValueError("передано неверное значение")

        if 0 >= key[0] >= 3 and 0 >= key[1] >= 3:
            raise IndexError('неверный индекс клетки')

        if self.pole[key[0]][key[1]]:
            self.pole[key[0]][key[1]].value = value

        else:
            raise ValueError('клетка уже занята')

    def clear(self):
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])


# dd = TicTacToe()
# dd[1, 1] = dd.CROSS
# s = dd[:, 1]
# print(s)
cl1 = Cell(-5)
cl2 = Cell("dede")
print(cl1, cl2)
