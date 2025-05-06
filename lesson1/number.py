"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    value: float

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, add_num):
        self.value = self.value + add_num


    def substract(self, sub_num):
        self.value = self.value - sub_num


# код для проверки 
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5
