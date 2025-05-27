"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""

from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        """Конструктор, принимающий числитель и знаменатель дроби"""
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

        # Приводим дробь к каноническому виду
        # Если знаменатель отрицательный, переносим знак в числитель
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Упрощаем дробь, деля на НОД
        common_divisor = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __repr__(self):
        """Магический метод, возвращающий строковое представление для создания объекта"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        """Магический метод, возвращающий строковое представление дроби"""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Магический метод для сложения дробей"""
        if isinstance(other, Fraction):
            # Складываем дроби: a/b + c/d = (a*d + c*b)/(b*d)
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            # Складываем дробь с целым числом
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Обратное сложение (когда дробь справа от оператора +)"""
        return self.__add__(other)

    def __eq__(self, other):
        """Проверка на равенство дробей"""
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        return False


# Пример использования:
if __name__ == "__main__":

    # код для проверки
    fraction1 = Fraction(1, 2)
    print(repr(fraction1))  # Fraction(1, 2)
    print(str(fraction1))  # 1/2

    fraction2 = Fraction(3, 4)
    fraction3 = fraction1 + fraction2
    print(fraction3)  # 5/4
