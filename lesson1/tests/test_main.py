import pytest
from lesson1.main import Product, Category


def test_product_initialization(sample_product):
    assert sample_product.name == "Продукт 1"
    assert sample_product.description == "Описание продукта 1"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Тестовая категория"
    assert sample_category.description == "Описание тестовой категории"
    assert sample_category.products == sample_products
    assert len(sample_category.products) == 3


def test_category_counters(reset_category_counters, sample_products):
    assert Category.category_count == 0
    assert Category.product_count == 0

    category = Category("Тест", "Описание", sample_products)

    assert Category.category_count == 1
    assert Category.product_count == len(sample_products)


@pytest.mark.parametrize("product_with_params", [
    ("Телефон", "Смартфон", 999.99, 5),
    ("Ноутбук", "Игровой ноутбук", 1999.99, 3),
    ("Наушники", "Беспроводные", 199.99, 20)
], indirect=True)
def test_different_products(product_with_params):
    assert isinstance(product_with_params, Product)
    assert product_with_params.price > 0
    assert product_with_params.quantity > 0


@pytest.mark.parametrize("category_with_products", [0, 1, 5, 10], indirect=True)
def test_categories_with_different_product_counts(reset_category_counters, category_with_products):
    num_products = len(category_with_products.products)
    assert Category.category_count == 1
    assert Category.product_count == num_products
