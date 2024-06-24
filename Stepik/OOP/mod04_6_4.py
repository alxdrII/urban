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


