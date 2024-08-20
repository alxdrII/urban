class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    # здесь добавляйте еще один магический метод для умножения
    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias * other
        return obj


# здесь объявляйте класс Linear
class Linear(Function):
    def __init__(self, k, b):
        self._k = k
        self._b = b

    def _get_function(self, x):
        pass


# ----------------------------------
f = Linear(1, 0.5)
f2 = f + 10   # изменение смещения (атрибут _bias)
y1 = f(0)     # 0.5
y2 = f2(0)    # 10.5

f = Linear(1, 0.5)
f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
y1 = f(0)     # 0.5
y2 = f2(0)    # 2.5