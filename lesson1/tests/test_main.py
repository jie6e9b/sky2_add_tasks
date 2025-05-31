import pytest
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from lesson1.main import Product, Smartphone, LawnGrass, Category


class TestSmartphoneInitialization:
    """Тесты инициализации класса Smartphone"""

    @pytest.fixture
    def smartphone_data(self):
        """Фикстура с данными для создания смартфона"""
        return {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8,
            "efficiency": 98.2,
            "model": "15",
            "memory": 512,
            "color": "Gray space"
        }

    @pytest.fixture
    def smartphone(self, smartphone_data):
        """Фикстура создания объекта Smartphone"""
        return Smartphone(
            smartphone_data["name"],
            smartphone_data["description"],
            smartphone_data["price"],
            smartphone_data["quantity"],
            smartphone_data["efficiency"],
            smartphone_data["model"],
            smartphone_data["memory"],
            smartphone_data["color"]
        )

    def test_smartphone_initialization_success(self, smartphone, smartphone_data):
        """Тест успешной инициализации смартфона"""
        # Проверяем атрибуты родительского класса Product
        assert smartphone.name == smartphone_data["name"]
        assert smartphone.description == smartphone_data["description"]
        assert smartphone.price == smartphone_data["price"]
        assert smartphone.quantity == smartphone_data["quantity"]

        # Проверяем специфичные атрибуты Smartphone
        assert smartphone.efficiency == smartphone_data["efficiency"]
        assert smartphone.model == smartphone_data["model"]
        assert smartphone.memory == smartphone_data["memory"]
        assert smartphone.color == smartphone_data["color"]

    def test_smartphone_is_product_instance(self, smartphone):
        """Тест что Smartphone является экземпляром Product"""
        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, Smartphone)

    def test_smartphone_inheritance(self):
        """Тест наследования класса Smartphone от Product"""
        assert issubclass(Smartphone, Product)

    def test_smartphone_str_method(self, smartphone):
        """Тест строкового представления смартфона"""
        expected_str = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
        assert str(smartphone) == expected_str

    def test_smartphone_price_property(self, smartphone):
        """Тест работы свойства price"""
        # Проверяем getter
        assert smartphone.price == 210000.0

        # Проверяем setter с корректным значением
        smartphone.price = 220000.0
        assert smartphone.price == 220000.0

    def test_smartphone_price_validation(self, smartphone, capsys):
        """Тест валидации цены смартфона"""
        # Попытка установить отрицательную цену
        smartphone.price = -1000
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        # Цена должна остаться прежней
        assert smartphone.price == 210000.0

        # Попытка установить нулевую цену
        smartphone.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_smartphone_with_different_parameters(self):
        """Тест создания смартфона с различными параметрами"""
        smartphone2 = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Black",
            150000.0,
            5,
            95.5,
            "Galaxy S23",
            256,
            "Black"
        )

        assert smartphone2.name == "Samsung Galaxy S23"
        assert smartphone2.memory == 256
        assert smartphone2.efficiency == 95.5

class TestLawnGrassInitialization:
    """Тесты инициализации класса LawnGrass"""

    @pytest.fixture
    def lawn_grass_data(self):
        """Фикстура с данными для создания газонной травы"""
        return {
            "name": "Газонная трава",
            "description": "Элитная трава для газона",
            "price": 500.0,
            "quantity": 20,
            "country": "Россия",
            "germination_period": "7 дней",
            "color": "Зеленый"
        }

    @pytest.fixture
    def lawn_grass(self, lawn_grass_data):
        """Фикстура создания объекта LawnGrass"""
        return LawnGrass(
            lawn_grass_data["name"],
            lawn_grass_data["description"],
            lawn_grass_data["price"],
            lawn_grass_data["quantity"],
            lawn_grass_data["country"],
            lawn_grass_data["germination_period"],
            lawn_grass_data["color"]
        )

    def test_lawn_grass_initialization_success(self, lawn_grass, lawn_grass_data):
        """Тест успешной инициализации газонной травы"""
        # Проверяем атрибуты родительского класса Product
        assert lawn_grass.name == lawn_grass_data["name"]
        assert lawn_grass.description == lawn_grass_data["description"]
        assert lawn_grass.price == lawn_grass_data["price"]
        assert lawn_grass.quantity == lawn_grass_data["quantity"]

        # Проверяем специфичные атрибуты LawnGrass
        assert lawn_grass.country == lawn_grass_data["country"]
        assert lawn_grass.germination_period == lawn_grass_data["germination_period"]
        assert lawn_grass.color == lawn_grass_data["color"]

    def test_lawn_grass_is_product_instance(self, lawn_grass):
        """Тест что LawnGrass является экземпляром Product"""
        assert isinstance(lawn_grass, Product)
        assert isinstance(lawn_grass, LawnGrass)

    def test_lawn_grass_inheritance(self):
        """Тест наследования класса LawnGrass от Product"""
        assert issubclass(LawnGrass, Product)

    def test_lawn_grass_str_method(self, lawn_grass):
        """Тест строкового представления газонной травы"""
        expected_str = "Газонная трава, 500.0 руб. Остаток: 20 шт."
        assert str(lawn_grass) == expected_str

    def test_lawn_grass_price_property(self, lawn_grass):
        """Тест работы свойства price"""
        # Проверяем getter
        assert lawn_grass.price == 500.0

        # Проверяем setter с корректным значением
        lawn_grass.price = 600.0
        assert lawn_grass.price == 600.0

    def test_lawn_grass_price_validation(self, lawn_grass, capsys):
        """Тест валидации цены газонной травы"""
        # Попытка установить отрицательную цену
        lawn_grass.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        # Цена должна остаться прежней
        assert lawn_grass.price == 500.0

    def test_lawn_grass_with_different_parameters(self):
        """Тест создания газонной травы с различными параметрами"""
        grass2 = LawnGrass(
            "Спортивная трава",
            "Трава для спортивных площадок",
            750.0,
            15,
            "Германия",
            "10 дней",
            "Темно-зеленый"
        )

        assert grass2.name == "Спортивная трава"
        assert grass2.country == "Германия"
        assert grass2.germination_period == "10 дней"

class TestProductSubclassesInteraction:
    """Тесты взаимодействия подклассов Product"""

    @pytest.fixture
    def smartphone(self):
        return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    @pytest.fixture
    def lawn_grass(self):
        return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    def test_different_subclasses_addition_error(self, smartphone, lawn_grass):
        """Тест что сложение разных подклассов вызывает ошибку"""
        with pytest.raises(TypeError) as exc_info:
            result = smartphone + lawn_grass
        assert "Сложение поддерживается только между объектами одного типа" in str(exc_info.value)
        assert "Smartphone" in str(exc_info.value)
        assert "LawnGrass" in str(exc_info.value)

    def test_same_subclass_addition(self):
        """Тест сложения объектов одного подкласса"""
        smartphone1 = Smartphone("Iphone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")
        smartphone2 = Smartphone("Iphone 14", "256GB", 180000.0, 5, 95.0, "14", 256, "Black")

        # Ожидаемый результат: (210000 * 8) + (180000 * 5) = 1680000 + 900000 = 2580000
        result = smartphone1 + smartphone2
        assert result == 2580000.0

        grass1 = LawnGrass("Трава 1", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Трава 2", "Описание", 400.0, 15, "Россия", "5 дней", "Зеленый")

        # Ожидаемый результат: (500 * 20) + (400 * 15) = 10000 + 6000 = 16000
        result = grass1 + grass2
        assert result == 16000.0

    def test_add_products_to_category(self, smartphone, lawn_grass):
        """Тест добавления подклассов в категорию"""
        category = Category("Смешанная категория", "Разные товары", [])

        # Оба объекта должны успешно добавиться
        category.add_product(smartphone)
        category.add_product(lawn_grass)

        # Проверяем что продукты добавились
        products_str = category.products
        assert "Iphone 15" in products_str
        assert "Газонная трава" in products_str

class TestEdgeCases:
    """Тесты граничных случаев"""

    def test_smartphone_zero_quantity(self):
        """Тест создания смартфона с нулевым количеством"""
        smartphone = Smartphone("Test Phone", "Test", 100000.0, 0, 90.0, "Test", 128, "Black")
        assert smartphone.quantity == 0

    def test_lawn_grass_zero_quantity(self):
        """Тест создания газонной травы с нулевым количеством"""
        grass = LawnGrass("Test Grass", "Test", 500.0, 0, "Test Country", "Test Period", "Green")
        assert grass.quantity == 0

    def test_smartphone_float_memory(self):
        """Тест создания смартфона с дробным значением памяти"""
        smartphone = Smartphone("Test", "Test", 100000.0, 5, 95.5, "Test", 128.5, "Black")
        assert smartphone.memory == 128.5

    def test_unicode_strings(self):
        """Тест с unicode строками"""
        smartphone = Smartphone("iPhone 📱", "Смартфон с эмодзи", 200000.0, 1, 99.9, "15 Pro", 512, "Золотой")
        assert smartphone.name == "iPhone 📱"
        assert smartphone.color == "Золотой"

        grass = LawnGrass("Трава 🌱", "Газонная трава с эмодзи", 500.0, 10, "Россия 🇷🇺", "7 дней", "Зелёный")
        assert grass.name == "Трава 🌱"
        assert grass.country == "Россия 🇷🇺"

@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy", "Описание", 50000, 10)

@pytest.fixture
def sample_product2():
    return Product("Iphone", "Описание 2", 100000, 20)

@pytest.fixture
def five_products():
    """Фикстура с 5 различными продуктами"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("iPhone 15 Pro", "512GB, Титановый, Pro камера", 210000.0, 8),
        Product("Xiaomi Redmi Note 12", "128GB, Синий, 50MP камера", 25000.0, 15),
        Product("Google Pixel 8", "256GB, Черный, AI камера", 85000.0, 12),
        Product("OnePlus 11", "256GB, Зеленый, Hasselblad камера", 75000.0, 7)
    ]

@pytest.fixture
def sample_category(sample_product):
    return Category("Смартфоны", "Описание категории", [sample_product])

def test_str_method_prod(sample_product):
    """Тест магического метода __str__ для продукта"""
    expected = "Samsung Galaxy, 50000 руб. Остаток: 10 шт."
    assert str(sample_product) == expected

def test_str_method_cat(sample_category):
    """Тест магического метода __str__ для категории"""
    expected = "Смартфоны, количество продуктов: 10 шт."
    assert str(sample_category) == expected

def test_add_method_(sample_product, sample_product2):
    expected = 2500000
    assert (sample_product.price * sample_product.quantity +
            sample_product2.price * sample_product2.quantity) == expected



def test_product_creation(sample_product):
    assert sample_product.name == "Samsung Galaxy"
    assert sample_product.description == "Описание"
    assert sample_product.price == 50000
    assert sample_product.quantity == 10


def test_product_price_setter(sample_product):
    # Проверка корректного изменения цены
    sample_product.price = 60000
    assert sample_product.price == 60000


def test_product_price_negative_value(sample_product, capsys):
    # Проверка попытки установить отрицательную цену
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 50000  # Цена не должна измениться


def test_product_price_zero(sample_product, capsys):
    # Проверка попытки установить нулевую цену
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 50000  # Цена не должна измениться


def test_new_product_class_method():
    # Проверка создания продукта через класс-метод
    product_data = {
        "name": "iPhone 13",
        "description": "Новый смартфон",
        "price": 70000,
        "quantity": 5
    }
    new_product = Product.new_product(product_data)

    assert new_product.name == "iPhone 13"
    assert new_product.description == "Новый смартфон"
    assert new_product.price == 70000
    assert new_product.quantity == 5


def test_category_creation(sample_category):
    # Проверка создания категории
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Описание категории"
    assert len(sample_category._Category__products) == 1


def test_category_add_product(sample_category):
    # Проверка добавления продукта в категорию
    initial_count = Category.product_count
    new_product = Product("Google Pixel", "Описание", 45000, 7)
    sample_category.add_product(new_product)

    assert len(sample_category._Category__products) == 2
    assert Category.product_count == initial_count + 1


def test_category_product_count():
    # Проверка подсчета продуктов и категорий
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    product1 = Product("Samsung", "Описание 1", 50000, 5)
    product2 = Product("Apple", "Описание 2", 70000, 3)

    category = Category("Новая категория", "Описание", [product1, product2])

    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2


def test_product_str_representation(sample_product):
    # Проверка строкового представления продукта
    expected_str = "Samsung Galaxy, 50000 руб. Остаток: 10 шт."
    assert str(sample_product) == expected_str



