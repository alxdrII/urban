"""
Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
прибывающих для заказа пищи и уходящих после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик,
употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию,
иначе он становится в очередь на ожидание.
"""
from queue import Queue
from time import sleep
from threading import Thread, Lock


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
        self.__lock = Lock()

    def customer_arrival(self, quantity=20):
        """моделирует приход посетителя (каждую секунду)"""

        for i in range(1, quantity+1):
            customer = Customer(i)
            # with self.__lock:
            #     self.queue.put(customer)
            print(f"Посетитель номер {customer.id} прибыл")
            self.serve_customer(customer)

            # customer_service = Thread(target=self.serve_customer, args=())

            sleep(1)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя.

        Проверяет наличие свободных столов, в случае наличия стола -
        начинает обслуживание посетителя (запуск потока),
        в противном случае - посетитель поступает в очередь.
        Время обслуживания 5 секунд."""

        free_table = next((x for x in self.tables if not x.is_busy), None)

        if free_table:
            free_table.is_busy = True
            print(f"Посетитель номер {customer.id} сел за стол {free_table.number}")
            sleep(5)
            free_table.is_busy = False
            print(f"Посетитель номер {customer.id} покушал и ушёл")

        else:
            self.queue.put(customer)
            print(f"Посетитель номер {customer.id} ожидает свободный стол")


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
