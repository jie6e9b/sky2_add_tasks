import pytest
from ..main_14_1 import Product, Category

@pytest.fixture
def sample_product():
    """Базовый экземпляр продукта для тестов"""
    return Product(name = "Продукт 1",
                   description = "Описание продукта 1",
                   price = 100.0,
                   quantity= 10
    )
@pytest.fixture
def sample_products():
    """Базовый экземпляр продукта для тестов"""
    return [
        Product(name = "Продукт 1",
                   description = "Описание продукта 1",
                   price = 100.0,
                   quantity= 10
                ),
        Product(name="Продукт 2",
                description="Описание продукта 2",
                price=50.0,
                quantity=5
                ),
        Product(name="Продукт 3",
                description="Описание продукта 3",
                price=75.0,
                quantity=15
                )
    ]

@pytest.fixture
def empty_product_list():
    """Пустой список продуктов."""
    return []


@pytest.fixture
def sample_category(sample_products):
    """Базовый экземпляр категории с продуктами."""
    return Category(
        name="Тестовая категория",
        description="Описание тестовой категории",
        products=sample_products
    )


@pytest.fixture
def empty_category(empty_product_list):
    """Категория без продуктов."""
    return Category(
        name="Пустая категория",
        description="Категория без продуктов",
        products=empty_product_list
    )


@pytest.fixture
def reset_category_counters():
    """Сбрасывает счетчики категорий перед тестами."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    # После теста также сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_with_params(request):
    """Параметризованная фикстура для создания продукта с разными параметрами."""
    name, description, price, quantity = request.param
    return Product(name=name, description=description, price=price, quantity=quantity)


@pytest.fixture
def category_with_products(request):
    """Параметризованная фикстура для создания категории с заданным количеством продуктов."""
    num_products = request.param
    products = [
        Product(f"Продукт {i}", f"Описание {i}", i * 100.0, i)
        for i in range(1, num_products + 1)
    ]
    return Category("Тестовая категория", "Описание", products)

