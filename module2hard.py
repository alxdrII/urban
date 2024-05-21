RANGE_MIN = 3
RANGE_MAX = 20

while True:
    key = input('Введите число от 3 до 20 или 0 для завершения: ')

    if not key.isnumeric():
        print('Неверный формат числа')
        continue

    key = int(key)
    if key == 0:
        print('До свидания!')
        break

    if not (RANGE_MIN <= key <= RANGE_MAX):
        print('Число вне диапазона')
        continue

    print('верно')
    break
