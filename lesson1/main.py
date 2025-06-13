from lesson1.base_product import BaseProduct
from lesson1.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, *args, **kwargs):
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            self.name = name
            self.description = description
            self.price = price
            self.quantity = quantity
            super().__init__(price, *args, **kwargs)

    @classmethod
    def new_product(cls, data):
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def get_product_info(self):
        """Базовая информация о продукте"""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'type': 'Базовый продукт'
        }

    def calculate_total_value(self):
        """Базовый расчет общей стоимости"""
        return self.price * self.quantity

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Сложение поддерживается только между объектами одного типа. "
                            f"Получены: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_product_info(self):
        """Расширенная информация о смартфоне"""
        base_info = super().get_product_info()
        base_info.update({
            'type': 'Смартфон',
            'model': self.model,
            'memory': f"{self.memory} ГБ",
            'color': self.color,
            'efficiency': f"{self.efficiency}%"
        })
        return base_info

    def calculate_total_value(self):
        """Расчет с учетом скидки на не эффективные смартфоны"""
        base_value = super().calculate_total_value()
        # Например, скидка 10% на не эффективные смартфоны
        if self.efficiency < 70:
            return base_value * 0.9
        else:
            return base_value


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_product_info(self):
        """Расширенная информация о газонной траве"""
        base_info = super().get_product_info()
        base_info.update({
            'type': 'Газонная трава',
            'country': self.country,
            'germination_period': f"{self.germination_period} дней",
            'color': self.color
        })
        return base_info

    def calculate_total_value(self):
        """Расчет с учетом сезонности для травы"""
        base_value = super().calculate_total_value()
        # Например, скидка для травы с долгим периодом прорастания
        if self.germination_period > 14:
            return base_value * 0.9  # 10% скидка
        return base_value


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """ Добавляет продукт в категорию с расширенной валидацией """
        # Проверка 1: Объект должен быть экземпляром Product или его наследника
        if not isinstance(product, Product):
            raise TypeError(
                f"Ошибка типа: ожидался объект класса Product или его наследника, "
                f"получен {type(product).__name__}. "
                f"Значение: {product}"
            )

        # Проверка 2: Класс объекта должен быть подклассом Product
        if not issubclass(type(product), Product):
            raise TypeError(
                f"Ошибка наследования: класс {type(product).__name__} "
                f"не является подклассом Product"
            )

        # Проверка 3: Дополнительная валидация продукта (от себя)
        if not hasattr(product, 'name') or not hasattr(product, 'price'):
            raise ValueError(
                f"Ошибка структуры: продукт должен иметь атрибуты 'name' и 'price'. "
                f"Отсутствуют в объекте {type(product).__name__}"
            )

        # Проверка 4: Валидация значений (от себя)
        if product.quantity < 0:
            raise ValueError(f"Количество продукта не может быть отрицательным: {product.quantity}")

        # Если все проверки пройдены - добавляем продукт
        self.__products.append(product)
        Category.product_count += 1
        print(f"✓ Продукт '{product.name}' ({type(product).__name__}) успешно добавлен в категорию '{self.name}'")

    def middle_price(self):
        """Возвращает среднюю цену продуктов в данной категории"""
        if len(self.__products) == 0:  # Проверяем продукты в этой категории
            return 0
        else:
            # Суммируем цены продуктов, а не сами объекты
            total_price = sum(product.price for product in self.__products)
            # print(f'теститруем {total_price}')
            return total_price / len(self.__products)

    @property
    def products(self):
        return '\n'.join(str(product) for product in self.__products)

    def __str__(self):
        product_sum = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {product_sum} шт."

if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
