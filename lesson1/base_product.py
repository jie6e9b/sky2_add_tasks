from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, price: float, *args, **kwargs):
        self.price = price  # вызывает сеттер
        super().__init__(*args, **kwargs)

    @abstractmethod
    def get_product_info(self):
        """Абстрактный метод для получения информации о продукте."""
        pass

    @abstractmethod
    def calculate_total_value(self):
        """Абстрактный метод для расчета общей стоимости продукта."""
        pass

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")