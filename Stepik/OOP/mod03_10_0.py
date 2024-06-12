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
        self.init()
        # self.is_human_win = False     # - возвращает True, если победил человек, иначе - False
        # self.is_computer_win = False  # - возвращает True, если победил компьютер, иначе - False
        # self.is_draw = False          # - возвращает True, если ничья, иначе - False

    def __getitem__(self, item):
        self.checking(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.checking(key)
        if not value in (self.COMPUTER_O, self.HUMAN_X):
            raise ValueError("Передано неверное значение")

        self.pole[key[0]][key[1]].value = value

    def __bool__(self):
        """возвращает True, если игра не окончена (никто не победил и есть свободные клетки)
        и False - в противном случае."""
        return not any(self.is_human_win, self.is_computer_win, self.is_draw)

    @staticmethod
    def checking(value: tuple):
        if 0 >= value[0] >= 2 and 0 >= value[1] >= 2:
            raise IndexError('некорректно указанные индексы'

    def init(self):
        self.pole = tuple([tuple([Cell(self.FREE_CELL) for _ in range(3)]) for _ in range(3)])
        self.is_human_win = False     # - возвращает True, если победил человек, иначе - False
        self.is_computer_win = False  # - возвращает True, если победил компьютер, иначе - False
        self.is_draw = False          # - возвращает True, если ничья, иначе - False

    def show(self):
        print()
        for i in range(3):
            print(*self.pole[i])

    def human_go(self):
        """реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);"""
        pass

    def computer_go(self):
        """- реализация хода компьютера (ставит случайным образом нолик в свободную клетку)."""
        pass


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
