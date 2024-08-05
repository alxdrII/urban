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


class Customer(Thread):
    """класс (поток) посетителя. Запускается, если есть свободные столы."""

    def __init__(self, id: int, cafe, table: Table = None):
        super().__init__()
        self.id = id
        self.cafe = cafe
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f"Посетитель номер {self.id} сел за стол {self.table.number}")
        sleep(5)
        self.table.is_busy = False
        print(f"Посетитель номер {self.id} покушал и ушёл")
        with self.cafe.lock:
            if not self.cafe.queue.empty():
                new_customer = self.cafe.queue.get()
                self.cafe.serve_customer(new_customer)


class Cafe:
    """класс для симуляции процессов в кафе"""

    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()
        self.lock = Lock()

    def customer_arrival(self, quantity=20):
        """моделирует приход посетителя (каждую секунду)"""

        for i in range(1, quantity+1):
            customer = Customer(i, cafe=self)
            print(f"Посетитель номер {customer.id} прибыл")
            self.serve_customer(customer)
            sleep(1)

    def serve_customer(self, customer):
        """моделирует обслуживание посетителя.

        Проверяет наличие свободных столов, в случае наличия стола -
        начинает обслуживание посетителя (запуск потока),
        в противном случае - посетитель поступает в очередь.
        Время обслуживания 5 секунд."""

        free_table = next((x for x in self.tables if not x.is_busy), None)

        if free_table:
            customer.table = free_table
            customer.start()

        else:
            with self.lock:
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
