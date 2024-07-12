def personal_sum(numbers: tuple):
    if not isinstance(numbers, tuple):
        raise TypeError

    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        summ, count_err = personal_sum(numbers)
        return summ / (len(numbers) - count_err)

    except ZeroDivisionError:
        return 0

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


sum_in = (10, 10, 'dd', 10, 'dd')
print(calculate_average(sum_in))
print(calculate_average('222'))
print(calculate_average(222))
