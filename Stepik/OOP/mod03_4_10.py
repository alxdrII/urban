class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        check_value = [isinstance(x, int) for row in matrix for x in row]
        if not (len(matrix) == len(matrix[0]) and all(check_value)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        # parts_x = len(matrix) // self.step[0]
        # parts_y = len(matrix) // self.step[0]

        result = []
        for y in range(0, len(matrix), self.step[1]):
            result.append([])
            for x in range(0, len(matrix), self.step[0]):
                result[].append()


mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
