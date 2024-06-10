class Cell:
    def __init__(self, is_free=True, value=0):
        self.is_free = is_free
        self.value = value

    def __bool__(self):
        return self.is_free

    def __setattr__(self, key, value):
        if key == 'value' and not self:
            raise ValueError('клетка уже занята')

        if key == 'value' and value > 0:
            self.is_free = False

        object.__setattr__(self, key, value)

    def __repr__(self):
        return str(self.value)


class TicTacToe:
    CROSS = 1
    ZERO = 2

    def __init__(self):
        self.pole = None
        self.clear()

    def clear(self):
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])

    def __getitem__(self, item):
        if isinstance(item[0], slice):
            print(item[0])

        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if 0 >= key[0] >= 3 and 0 >= key[1] >= 3:
            raise IndexError('неверный индекс клетки')

        self.pole[key[0]][key[0]].value = value


dd = TicTacToe()
dd[1, 1] = dd.CROSS
s = dd[:, 1]
print(s)

