"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
которое можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""


class MyList:
    def __init__(self, data):
        """Конструктор, принимающий список элементов"""
        if isinstance(data, list):
            self.data = data.copy()  # Создаем копию, чтобы избежать изменения оригинала
        else:
            raise TypeError("Аргумент должен быть списком")

    def __repr__(self):
        """Магический метод, возвращающий строковое представление для создания нового объекта"""
        return f"MyList({self.data!r})"

    def __str__(self):
        """Магический метод, возвращающий строковое представление списка"""
        return str(self.data)

    def __len__(self):
        """Магический метод, возвращающий длину списка"""
        return len(self.data)

    def __add__(self, other):
        """Магический метод для сложения списков, возвращает новый MyList"""
        if isinstance(other, MyList):
            return MyList(self.data + other.data)
        elif isinstance(other, list):
            return MyList(self.data + other)
        else:
            raise TypeError("Можно складывать только с MyList или list")


# Пример использования:
if __name__ == "__main__":
     # код для проверки
    my_list1 = MyList([1, 2, 3])
    print(repr(my_list1))  # MyList([1, 2, 3])
    print(str(my_list1))  # [1, 2, 3]
    print(len(my_list1))  # 3

    my_list2 = MyList([4, 5, 6])
    my_list3 = my_list1 + my_list2
    print(my_list3)  # [1, 2, 3, 4, 5, 6]
