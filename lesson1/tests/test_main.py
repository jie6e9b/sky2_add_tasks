import pytest
from lesson1.main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy", "Описание", 50000, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Смартфоны", "Описание категории", [sample_product])


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


