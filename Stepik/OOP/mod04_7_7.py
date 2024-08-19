class Note:

    NOTES = ('до', 'ре', 'ми', 'фа', 'соль', "ля", 'си')

    def __init__(self, name, ton):
        if not (name in self.NOTES and -1 >= ton >= 1):
            raise ValueError('недопустимое значение аргумента')

        self._name = name
        self._ton = ton


class Notes:

    __instance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        self._do = 0


nn = Notes()
print(nn._do)
