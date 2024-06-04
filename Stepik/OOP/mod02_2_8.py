# https://stepik.org/lesson/701984/step/10?unit=702085
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
        # for i in range(3):
        #     obj = obj.left if i else obj.right
            

        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [0, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)
