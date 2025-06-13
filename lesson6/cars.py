"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime

class Car:
    def __init__(self, make, model, year):
        current_year = datetime.datetime.now().year
        if year > current_year:
            raise ValueError("год должен быть не позднее текущего")
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"

if __name__ == '__main__':
    # код для проверки
    car3 = Car('Toyota', 'Corolla', 2022)


    try:
        car1 = Car('Toyota', 'Corolla', 2022)
        print(f"Создана машина: {car1}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        car2 = Car('Toyota', 'Corolla', 3000)
        print(f"Создана машина: {car2}")
    except ValueError as e:
        print(f"Ошибка: {e}")