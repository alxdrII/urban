import copy
from random import randint, shuffle


class Ship:
    """Корабль"""

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp  # ориентация корабля: 1 - горизонтальная (x); 2 - вертикальная (y)
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length  # попадания: 1 - небыло; 2 - было

    def __len__(self):
        return self._length

    @property
    def tp(self):
        return self._tp

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        """перемещение корабля в направлении его ориентации на 'go' клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону
        на одну клетку); движение возможно только если флаг _is_move = True"""

        if self._is_move:
            x = go if self._tp == 1 else 0
            y = go if self._tp == 2 else 0
            self.set_start_coords(x+self._x, y+self._y)

    def is_collide(self, other):
        """
        проверка на столкновение с другим кораблем ship (столкновением считается,
        если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;

        """
        o_x, o_y = other.get_start_coords()
        # область чувствительности нашего корабля
        x1, y1 = self._x - 1, self._y - 1
        x2, y2 = self._x + (self._length if self._tp == 1 else 1), self._y + (self._length if self._tp == 2 else 1)

        result = False

        for i in range(len(other)):
            if other.tp == 1:
                if x1 <= o_x + i <= x2 and y1 <= o_y <= y2:
                    result = True
                    break
            elif other.tp == 2:
                if x1 <= o_x <= x2 and y1 <= o_y + i <= y2:
                    result = True
                    break

        return result

    def is_out_pole(self, size):
        """
        проверка на выход корабля за пределы игрового поля (size - размер игрового поля);
        возвращается True, если корабль вышел из игрового поля и False - в противном случае

        """
        return self._x < 0 or self._y < 0 or (self._x + self._length) > size or (self._y + self._length) > size

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        if self._is_move and value == 2:
            self._is_move = False   # при попадании, корабль перестаёт двигаться

        self._cells[key] = value


class GamePole:
    """ Игровое поле игры 'Морской бой' """

    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        """
        начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship):
        однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей
        должна быть случайной).

        """
        # создаем предварительный список размеров кораблей
        len_ships = []
        for i in range(1, 5):
            for k in range(i, 5):
                len_ships.append(i)

        len_ships.reverse()    # расмещаем начиная с самого большого корабля

        self._ships.clear()

        # формируем список кораблей с учетом столкновений и выхода за пределы поля
        mx = self._size - 1
        for i in len_ships:
            ship_is_no_fit = True
            while ship_is_no_fit:
                ship_new = Ship(i, randint(1, 2), x=randint(0, mx), y=randint(0, mx))
                # если корабль не выходит за пределы поля и не столкнулся с другими кораблями, то признаем его годным
                if not (ship_new.is_out_pole(self._size) or any(ship_new.is_collide(ship) for ship in self._ships)):
                    self._ships.append(ship_new)
                    ship_is_no_fit = False # выходим из цикла while

    def get_ships(self):
        return self._ships

    def move_ships(self):
        """перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад)
        в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или
        пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения
        невозможны), оставаться на месте;"""
        for ship in self._ships:
            ship_new = copy.deepcopy(ship)
            ship_new.move(1)
            if not (ship_new.is_out_pole(self._size) or any(ship_new.is_collide(s) for s in self._ships if s != ship)):
                ship.move(1)
                continue

            ship_new = copy.deepcopy(ship)
            ship_new.move(-1)
            if not (ship_new.is_out_pole(self._size) or any(ship_new.is_collide(s) for s in self._ships if s != ship)):
                ship.move(-1)
                continue

    def show(self):
        pole = self.get_pole()
        for i in range(self._size):
            print(*pole[i])

    def get_pole(self):
        """получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов."""

        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x1, y1 = ship.get_start_coords()
            if ship.tp == 1:
                for x in range(x1, x1 + len(ship)):
                    pole[y1][x] = 1

            elif ship.tp == 2:
                for y in range(y1, y1 + len(ship)):
                    pole[y][x1] = 2

        return pole


gp = GamePole(10)
gp.init()
gp.show()
gp.move_ships()
print()
gp.show()
