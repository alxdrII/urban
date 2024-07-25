from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека"""

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека"""


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._bottom = None

    def push_back(self, obj):
        # не будем добавлять объект, который уже есть в стеке
        if self._top is None:
            self._top = obj
            self._bottom = obj

        else:
            self._bottom._next = obj
            self._bottom = obj

    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    # def __eq__(self, other):
    #     return self._data == other.data
    #
    # def __hash__(self):
    #     return hash(self._data)


# ----
st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)