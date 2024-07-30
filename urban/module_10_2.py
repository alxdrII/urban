from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power, enemies=100):
        super().__init__()
        self.name = name
        self.power = power
        self.__enemies = enemies

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.__enemies:
            self.__enemies -= self.power
            self.__enemies = 0 if self.__enemies < 0 else self.__enemies
            sleep(1)
            days += 1
            print(f"{self.name} сражается {days}..., осталось {self.__enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")
        
        
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")