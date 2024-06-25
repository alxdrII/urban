class Digit:
    def __init__(self, value):
        self.value = None
        if self._check(value):
            self.value = value

        else:
            raise TypeError("значение не соответствует типу объекта")

    def _check(self, value):
        if isinstance(value, (int, float)):
            return True

        return False


class Integer(Digit):
    def _check(self, value):
        if isinstance(value, int):
            return True

        return False


class Float(Digit):
    def _check(self, value):
        if isinstance(value, float):
            return True

        return False


class Positive(Digit):
    def _check(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            return True

        return False


class Negative(Digit):
    def _check(self, value):
        if isinstance(value, (int, float)) and value < 0:
            return True

        return False


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


# x1 = Digit(0)
# x2 = Digit(2.2)
# x3 = Digit(-8.5)
# x4 = Digit(False)

in1 = Positive(-4)
