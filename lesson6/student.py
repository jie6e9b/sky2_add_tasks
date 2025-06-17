"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, rates):
        self.name = name
        self.course = course
        self.rates = rates

    def avg_rate(self):
        if len(self.rates) == 0:
            return 0
        else:
            return sum(self.rates) / len(self.rates)


if __name__ == '__main__':  # Исправляем условие
    # код для проверки
    student1 = Student('Ivan', 1, [5, 4, 5, 5])  # course должен быть числом
    print(student1.avg_rate())  # Выведет: 4.75

    student2 = Student('Ivan', 1, [])
    print(student2.avg_rate())  # Выведет: 0