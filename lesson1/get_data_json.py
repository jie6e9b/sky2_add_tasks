import json
from typing import List, Dict
from lesson1.main import Product, Category

def load_data_from_json(filename: str) -> List[Category]:
    """ Загрузка данных из JSON-файла и создание объектов категорий и товаров
    :param filename: Путь к JSON-файлу
    :return: Список категорий """

    try:
        # Открываем и читаем JSON-файл
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Список для хранения категорий
        categories = []

        # Обработка каждой категории
        for category_data in data:
            # Создаем список товаров для текущей категории
            products = []

            # Обработка товаров в категории
            for product_data in category_data.get('products', []):
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity']
                )
                products.append(product)

            # Создаем объект категории
            category = Category(
                name=category_data['name'],
                description=category_data['description'],
                products=products
            )

            categories.append(category)

        return categories

    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле {filename}.")
        return []
    except KeyError as e:
        print(f"Ошибка: Отсутствует обязательное поле в данных - {e}")
        return []


def main():
    # Загрузка данных из JSON-файла
    filename = '/Users/vladimir/PycharmProjects/tmp/tests/sky2_add_tasks/lesson1/data/products.json'
    categories = load_data_from_json(filename)

    # Вывод загруженных данных
    for category in categories:
        print(category)
        print("Товары в категории:")
        for product in category.products:
            print(product)
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()