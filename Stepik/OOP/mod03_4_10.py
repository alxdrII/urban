class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        is_err = False
        if len(matrix) != len(matrix[0]):
            is_err = True

        check_value = [isinstance(x, int) for row in matrix for x in row]
        if is_err or (not all(check_value)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        print("OK")


sp = MaxPooling()
dd = sp([[1, 1], [5, 5], [5, 5]])