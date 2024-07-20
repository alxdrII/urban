from random import choice

# ----- Lambda-функция: ----------
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print("---- Lambda-функция:")
print(result)
print()

# ----- Замыкание: ----------
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.writelines(map(lambda x: str(x)+'\n', data_set))

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print("---- Замыкание:")
print("см файл example.txt")
print()

# ----- Метод __call__: --------------
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print("---- Метод __call__:")
print(first_ball())
print(first_ball())
print(first_ball())
