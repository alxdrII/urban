from random import randint, shuffle


class Ship:
    """Корабль"""

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp  # ориентация корабля: 1 - горизонтальная (x); 2 - вертикальная (y)
        self._x = x
        self._y = y
        self.is_move = True
        self._cells = [1] * length  # попадания: 1 - небыло; 2 - было

    def __setattr__(self, key, value):
        if key == '_cells' and self.is_move and value == 2:
            # при попадании, корабль перестаёт двигаться
            self.is_move = False

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

        if self.is_move:
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
        # область чувствительности корабля
        x1, y1 = self._x - 1, self._y - 1
        x2, y2 = self._x + self._length if self._tp == 1 else 1, self._y + self._length if self._tp == 2 else 1

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
        return self._x < 0 or self._y < 0 or self._x + self._length >= size or self._y + self._length >= size

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
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

        shuffle(len_ships)    # перемешиваем для рандомности, но можно и без этого

        # размещаем случайно корабли на поле
        self._ships.clear()
        for i in len_ships:
            x = randint(0, self._size-1)
            y = randint(0, self._size-1)



    def get_ships(self):
        return self._ships

    def move_ships(self):
        """перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад)
        в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или
        пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения
        невозможны), оставаться на месте;"""

        pass

    def show(self):
        pass

    def get_pole(self):
        """получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов."""
