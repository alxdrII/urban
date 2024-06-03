class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__left

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        pass

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        pass
