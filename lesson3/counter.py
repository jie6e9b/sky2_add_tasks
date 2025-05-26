"""
Напишите класс Counter, имеющий следующие методы:

- __init__(self): конструктор, создающий счетчик и устанавливающий его значение в 0;
- __call__(self): магический метод, который позволяет использовать объект класса Counter как функцию, возвращающую текущее значение счетчика;
- increment(self): метод, увеличивающий значение счетчика на 1.
"""


class Counter:
    def __init__(self):
        """Конструктор, создающий счетчик и устанавливающий его значение в 0"""
        self.value = 0

    def increment(self):
        """Увеличивает значение счетчика на 1"""
        self.value += 1

    def decrement(self):
        """Уменьшает значение счетчика на 1"""
        self.value -= 1

    def get_value(self):
        """Возвращает текущее значение счетчика"""
        return self.value

    def reset(self):
        """Сбрасывает счетчик в 0"""
        self.value = 0

    def __str__(self):
        """Строковое представление счетчика"""
        return f"Counter: {self.value}"

    def __repr__(self):
        """Представление для отладки"""
        return f"Counter(value={self.value})"


# Пример использования:
if __name__ == "__main__":
    # Создаем счетчик
    counter = Counter()
    print(counter)  # Counter: 0

    # Увеличиваем значение
    counter.increment()
    counter.increment()
    print(counter.get_value())  # 2

    # Уменьшаем значение
    counter.decrement()
    print(counter)  # Counter: 1

    # Сбрасываем
    counter.reset()
    print(counter)  # Counter: 0




# код для проверки 
counter = Counter()
print(counter())  # 0

counter.increment()
print(counter())  # 1

counter.increment()
print(counter())  # 2
