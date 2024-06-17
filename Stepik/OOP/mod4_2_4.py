class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __eq__(self, other):
        return self.name == other.name \
            and self.price == other.price \
            and self.weight == other.weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, seq=None):
        if not (seq is None or type(seq) == dict):
            raise TypeError('аргумент должен быть словарем')

        super().__init__(seq)

    @staticmethod
    def check_on_Thing(key):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

        return True


