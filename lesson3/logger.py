"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""

import datetime


class Logger:
    def __init__(self, filename):
        """
        Конструктор, принимающий имя файла для записи логов

        Args:
            filename (str): имя файла для записи логов
        """
        self.filename = filename

    def __call__(self, message):
        """
        Магический метод, позволяющий использовать объект как функцию
        Записывает сообщение в файл с временной меткой

        Args:
            message (str): сообщение для записи в лог
        """
        # Получаем текущее время
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Формируем строку лога с временной меткой
        log_entry = f"[{timestamp}] {message}\n"

        # Записываем в файл (режим 'a' для добавления)
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(log_entry)

# код для проверки
if __name__ == "__main__":
    logger = Logger("log.txt")
    logger("This is a test message.")
