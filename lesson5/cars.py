"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:
    def __init__(self, brand, model, year_build):
        self.brand = brand
        self.model = model
        self.year_build = year_build

    def get_set_del(self):
        """Метод для тестирования производительности"""
        # Получение
        brand = self.brand
        model = self.model
        year = self.year_build

        # Установка
        self.brand = "Test"
        self.model = "Test"
        self.year_build = 2023

        # Возврат исходных значений
        self.brand = brand
        self.model = model
        self.year_build = year


class CarSlots:
    __slots__ = ['brand', 'model', 'year_build']
    def __init__(self,brand, model, year_build):
        self.brand = brand
        self.model = model
        self.year_build = year_build

    def get_set_del(self):
        """Метод для тестирования производительности"""
        # Получение
        brand = self.brand
        model = self.model
        year = self.year_build

        # Установка
        self.brand = "Test"
        self.model = "Test"
        self.year_build = 2023

        # Возврат исходных значений
        self.brand = brand
        self.model = model
        self.year_build = year


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)

print(f"⏱️  Обычный класс: {t1:.6f} секунд")
print(f"🚀 Класс с __slots__: {t2:.6f} секунд")
print(f"📈 Улучшение производительности: {((t1-t2)/t1*100):.2f}%")
