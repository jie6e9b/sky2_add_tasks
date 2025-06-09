from lesson1.base_product import BaseProduct
import pytest

# Нельзя создать экземпляр BaseProduct напрямую
def test_base_product_instantiation_fails():
    with pytest.raises(TypeError, match="Can't instantiate abstract class BaseProduct without an implementation for abstract methods"):
        BaseProduct(price=1000)


# Фиктивный подкласс для тестирования
class DummyProduct(BaseProduct):
    def get_product_info(self):
        return {"name": "dummy"}

    def calculate_total_value(self):
        return self.price * 2


def test_price_getter_setter_valid():
    product = DummyProduct(price=1000)
    assert product.price == 1000
    product.price = 2500
    assert product.price == 2500


def test_price_setter_invalid_zero():
    product = DummyProduct(price=1000)
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = 0


def test_price_setter_invalid_negative():
    product = DummyProduct(price=1000)
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = -500

# Наследник обязан реализовать все абстрактные методы (get_product_info и calculate_total_value)
def test_incomplete_subclass_instantiation_fails():
    class IncompleteProduct(BaseProduct):
        pass

    with pytest.raises(TypeError, match="Can't instantiate abstract class IncompleteProduct"):
        IncompleteProduct(price=1000)



