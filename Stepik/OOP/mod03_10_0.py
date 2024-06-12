class Cell:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        if hasattr(self, 'value'):
            return self.value == 0
        else:
            return True

    def __setattr__(self, key, value):
        if key == 'value' and not self:
            raise ValueError('клетка уже занята')

        object.__setattr__(self, key, value)

    def __repr__(self):
        return str(self.value)


class TicTacToe:
    FREE_CELL = 0   # свободная клетка
    HUMAN_X = 1     # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = None
        self.clear()

    def __getitem__(self, item):
        self.checking(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.checking(key)
        self.pole[key[0]][key[1]].value = value

    @staticmethod
    def checking(value: tuple):
        if 0 >= value[0] >= 2 and 0 >= value[1] >= 2:
            raise IndexError('некорректно указанные индексы')

    def clear(self):
        self.pole = tuple([tuple([Cell(self.FREE_CELL) for _ in range(3)]) for _ in range(3)])

    def show(self):
        for i in range(3):
            print(*self.pole[i])


dd = TicTacToe()
dd[0, 0] = 1
dd[1, 0] = 2
dd.show()
dd[2, 0] = 555
dd.show()

