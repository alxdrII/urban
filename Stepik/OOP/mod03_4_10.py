class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        if any([len(matrix) != len(matrix[x]) for x in range(len(matrix))]):
            raise ValueError("Неверный формат для первого параметра matrix.")

        if not all([isinstance(x, (int, float)) for row in matrix for x in row]):
            raise ValueError("Неверный формат для первого параметра matrix.")

        result_x = self.out_matrix_len(len(matrix), self.step(0), self.size(0))
        result_y = self.out_matrix_len(len(matrix), self.step(1), self.size(1))

        result = []
        for y in range(result_y):
            result.append([])
            for x in range(result_x):
                result[y].append(self._max_in_win(matrix, x * self.size[0], y * self.size[1]))

        return result

    @staticmethod
    def out_matrix_len(len_matrix: int, step: int, size: int):
        a = len_matrix // step
        if len_matrix % step >= size:
            a += 1
            
        return a


    def _max_in_win(self, matrix: list, mx: int, my: int):
        tmp = []
        for y in range(my, self.size[1] + my):
            for x in range(mx, self.size[0] + mx):
                tmp.append(matrix[y][x])

        return max(tmp)


mp = MaxPooling(step=(1, 1), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)

# res = mp([[5, 0, 88, 2, 7, 65], [1, 33, 7, 45, 0, 1], [54, 8, 2, 38, 22, 7], [73, 23, 6, 1, 15, 0],
#           [4, 12, 9, 1, 76, 6], [0, 15, 10, 8, 11, 78]])    # [[33, 88, 65], [73, 38, 22], [15, 10, 78]]
# print(res)
#
# res = mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]]) # [[7]]
# print(res)
