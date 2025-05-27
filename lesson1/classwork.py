from logging.config import stopListening

class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first},{self.last},{self.pay})"

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first + ' ' + self.last)


emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Petr', 'Petrov', 100000)
print(emp_1 + emp_2)
print(emp_1)
print(emp_1.__repr__())
print(len(emp_1))

class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])


class StripChars:

    def __init__(self,chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return args[0].strip(self.chars)

st1 = StripChars('?')
st2 = StripChars('!')

res = st2("?Example?")

print(res)

class EvenRange:

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.current_value = -2
        return self

    def __next__(self):
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration


for i in EvenRange(7):
    print(i)

    # 0, 2, 4, 6

class MyOpen:
    def __init__(self, filename, mode='r'):
        """
        Класс, который создает объект, который можно использовать
        вместо open(), чтобы автоматически закрывать файл.
        :param filename: имя файла
        :param mode: режим открытия файла (по умолчанию 'r')
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """
        Метод, который вызывается при входе в блок контекста.
        Он открывает файл и возвращает файловый дескриптор.
        :return: файловый дескриптор
        """
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, который вызывается при выходе из блока контекста.
        Он закрывает файл.
        """
        self.fp.close()
#
# with MyOpen('text.txt', 'r') as fp:  # Открываем файл
#     print(fp.read())  # Читаем файл



class MyContext:
    def __enter__(self):
        print("Entering context")

    def __exit__(self, type, value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside context")

