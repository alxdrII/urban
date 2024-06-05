class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        obj = root
        if x[0]:
            obj = obj.left
            if x[1]:
                obj = obj.left
            else:
                obj = obj.right
        else:
            obj = obj.right
            if x[2]:
                obj = obj.left
            else:
                obj = obj.right

        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj
