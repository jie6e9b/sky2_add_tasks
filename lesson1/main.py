class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data):
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

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


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    @property
    def products(self):
        return '\n'.join(str(product) for product in self.__products)

    def __str__(self):
        product_sum = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {product_sum} шт."


if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
