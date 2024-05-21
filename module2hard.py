RANGE_MIN = 3
RANGE_MAX = 20

while True:
    key = input('Введите число от 3 до 20 или 0 для завершения: ')

    if not key:
        key = '0'

    if not key.isnumeric():
        print('Неверный формат числа.\n')
        continue

    key = int(key)

    if key == 0:
        print('До свидания!')
        break

    if not (RANGE_MIN <= key <= RANGE_MAX):
        print('Число вне диапазона.\n')
        continue

    print(f'Пароль для числа {key} - ', end='')
    for i in range(1, key):
        for j in range(1, key):
            if key % (i + j) == 0 and i < j:
                print(i, j, end='', sep='')

    print('\n')
