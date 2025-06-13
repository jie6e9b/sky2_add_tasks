"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- имя
- возраст
- зарплата

Напишите класс Employee, у которого конструктор проверяет, что возраст не меньше 18 и не больше 127 лет.
В случае, если возраст не укладывается в заданные рамки, вызвать исключение ValueError и прервать выполнение программы.
Также в конструкторе необходимо проверять уровень зарплаты, который должен быть не меньше 16242. Вызывать ValueError
исключение.

Вызванные исключения должны пояснять в чем именно произошла ошибка.
"""


class Employee:
    def __init__(self, name, age, salary):
        if age < 18 or age > 127:
            raise ValueError('возраст должен быть в пределах от 18 до 127 лет')
        if salary < 16242:
            raise  ValueError('зараплата должна быть больше прожиточного минимума 16242р')

        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"{self.name}, возраст: {self.age}, зпшка: {self.salary}"


if __name__ == '__main__':

    # код для проверки
    try:
        employee = Employee('John', 30, 5000)
    except ValueError as e:
        print(e)
        # raises ValueError('Оплата труда не может быть меньше 16242')

    try:
        employee = Employee("Jane", 17, 50000)
    except ValueError as e:
        print(e)
        # raises ValueError('Возраст должен быть не меньше 18 и не больше 127')

    try:
        employee = Employee("Kate", 175, 50000)
        # raises ValueError('Возраст должен быть не меньше 18 и не больше 127')
    except ValueError as e:
        print(e)