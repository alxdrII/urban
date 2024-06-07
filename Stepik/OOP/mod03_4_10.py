class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        check_value = [isinstance(x, int) for row in matrix for x in row]
        if not (len(matrix) == len(matrix[0]) and all(check_value)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        result_x = len(matrix) // self.step[0]
        result_y = len(matrix) // self.step[1]

        result = []
        for y in range(result_y):
            result.append([])
            for x in range(result_x):
                result[y].append(self.max_in_win(matrix, x * self.size[0], y * self.size[1]))

        return result

    def max_in_win(self, matrix: list, mx: int, my: int):
        tmp = []
        for y in range(my, self.size[1] + my):
            for x in range(mx, self.size[0] + mx):
                tmp.append(matrix[y][x])
        
        return max(tmp)


mp = MaxPooling(step=(3, 3), size=(3, 3))
#res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
res = mp([[1, 2, 3, 4, 10], [5, 6, 7, 8, 20], [9, 8, 7, 6, 30], [5, 4, 3, 2, 40], [50, 60, 70, 80]])  # [[6, 8], [9, 7]]
print(res)
