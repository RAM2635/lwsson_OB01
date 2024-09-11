# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой
# сети имеет свои особенности, но также существуют общие характеристики, такие как адрес,
# название и ассортимент товаров.
# Ваша задача — создать
# класс `Store`, который можно будет использовать для создания различных магазинов.
# 1. Создай класс `Store`.
# 2. Создай несколько объектов класса `Store`.
#    Создай не менее трёх различных магазинов с разными названиями, адресами и добавь
#    в каждый из них несколько товаров.
# 3. Протестировать методы.
#    Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
#    обнови цену, убери товар и запрашивай цену.

class Store:
    """Создаём класс Store"""

    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым ассортиментом."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' успешно добавлен в магазин '{self.name}' по цене {price:.2f}.")

    def remove_item(self, item_name):
        """Удалить товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' успешно удален из магазина '{self.name}'.")
        else:
            print(f"Ошибка: Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_price(self, item_name):
        """Получить цену товара по его названию."""
        price = self.items.get(item_name)
        if price is not None:
            return price
        else:
            print(f"Ошибка: Товар '{item_name}' отсутствует в магазине '{self.name}'.")
            return None

    def update_price(self, item_name, new_price):
        """Обновить цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' в магазине '{self.name}' обновлена до {new_price:.2f}.")
        else:
            print(f"Ошибка: Товар '{item_name}' не найден в магазине '{self.name}'.")


# Создание объектов класса Store
store1 = Store("Магазин 1", "Улица 1, дом 1")
store2 = Store("Магазин 2", "Улица 2, дом 2")
store3 = Store("Магазин 3", "Улица 3, дом 3")

# Добавление товаров в магазины
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store2.add_item("Апельсины", 0.85)
store3.add_item("Груши", 1.0)
store3.add_item("Киви", 1.5)

# Тестирование методов для магазина store1
print("\nТестирование методов для магазина:", store1.name)

# Получение цены товара
price = store1.get_price("Яблоки")
if price is not None:
    print(f"Цена товара 'Яблоки' в магазине '{store1.name}': {price:.2f}")

# Обновление цены товара
store1.update_price("Яблоки", 0.6)

# Удаление товара
store1.remove_item("Бананы")

# Проверка цены удаленного товара
price_bananas = store1.get_price("Бананы")
if price_bananas is None:
    print(f"Товар 'Бананы' больше не доступен в магазине '{store1.name}'.")
