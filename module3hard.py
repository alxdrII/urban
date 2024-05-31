def calculate_structure_sum(*args):
    result = 0

    for values in args:
        if isinstance(values, int):
            result += values

        elif isinstance(values, float):
            result += int(values)

        elif isinstance(values, str):
            result += len(values)

        elif type(values) in (list, tuple, set):
            result += calculate_structure_sum(*values)

        elif isinstance(values, dict):
            result += calculate_structure_sum(*values.keys()) + calculate_structure_sum(*values.values())

    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
