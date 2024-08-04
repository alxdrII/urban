"""
Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
прибывающих для заказа пищи и уходящих после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик,
употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию,
иначе он становится в очередь на ожидание.
"""
from queue import Queue
from time import sleep
from threading import Thread


class Table:
    """класс для столов"""

    def __init__(self, number: int, is_busy: bool = False):
        self.__number = number
        self.is_busy = is_busy

    @property
    def number(self):
        return self.__number


class Customer:
    """класс (поток) посетителя. Запускается, если есть свободные столы."""

    def __init__(self, id: int):
        self.id = id

class Cafe:
    """класс для симуляции процессов в кафе"""

    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()

    def customer_arrival(self, quantity=20):
        """моделирует приход посетителя (каждую секунду)"""

        for i in range(1, quantity+1):
            print(f"Посетитель номер {i} прибыл")
            self.serve_customer(Customer(i))
            sleep(1)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя.

        Проверяет наличие свободных столов, в случае наличия стола -
        начинает обслуживание посетителя (запуск потока),
        в противном случае - посетитель поступает в очередь.
        Время обслуживания 5 секунд."""
        if





# ------------------------- test --------------
# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
