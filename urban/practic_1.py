# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Реализуем модель доставки грузов

# Дорога - хранит расстояния между объектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс - Машина
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#   ёмкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоять под погрузкой/разгрузкой
#   ехать со скоростью

# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content=0):
        self.name = name
        self.content = content  # Количество того чего храним на данном складе
        self.road_out = None    # дорога
        self.queue_in = []      # очередь из пустых машин готовых для загрузки
        self.queue_out = []     # очередь из машин готовых к отправке

    def __str__(self):
        return 'Склад {} груза {}'.format(self.name, self.content)

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print('{} прибыл грузовик {} '.format(self.name, truck))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('{} грузовик готов {} '.format(self.name, truck))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} топлива {}'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        print('{} заправился {}'.format(self.model, self.fuel))


class Truck(Vehicle):
    fuel_rate = 50  # трата доплива за 1 раз (цикл, час..)

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space  # Грузовместимость
        self.cargo = 0
        self.velocity = 100  # Скорость движения км/час
        self.place = None    # текущее местонахождение (дорога или склад)
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + ' груза {}'.format(self.cargo)

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось {}'.format(self.model, self.distance_to_target))
        else:
            self.place = self.place.end   # Конечная точка назначения дороги - склад
            self.place.truck_arrived(self) # регистрируемся на складе на который прибыли
            print('{} доехал '.format(self.model))

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print('{} выехал в путь'.format(self.model))

    def act(self):
        if self.fuel <= 10:  # Мало топлива, надо заправится
            self.tank_up()
        elif isinstance(self.place, Road): # Если грузовик в дороге, то он едет дальше
            self.ride()


class AutoLoader(Vehicle):
    fuel_rate = 30

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + ' груза {}'.format(self.truck)

    def act(self):
        if self.fuel <= 10:  # Мало топлива, надо заправится
            self.tank_up()
        elif self.truck is None: # Если грузовика нет в наличии, то пусть дают следующий
            self.truck = self.warehouse.get_next_truck()
            print('{} взял в работу {}'.format(self.model, self.truck))
        elif self.role == 'loader':
            self.load()
        else:
            self.unload()

    def load(self):
        self.fuel -= self.fuel_rate
        truck_cargo_rect = self.truck.body_space - self.truck.cargo
        if truck_cargo_rect >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rect
            self.truck.cargo += truck_cargo_rect
        print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.warehouse.content += self.bucket_capacity
            self.truck.cargo -= self.bucket_capacity
        else:
            self.warehouse.content += self.truck.cargo
            self.truck.cargo -= self.truck.cargo
        print('{} разгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

truck_1 = Truck('КАМАЗ', body_space=5000)
truck_2 = Truck('ГАЗ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint('---------------- Час {} -----------------'.format(hour), color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')
