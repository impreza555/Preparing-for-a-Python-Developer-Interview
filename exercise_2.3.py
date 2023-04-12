class ItemDiscount:
    """
    Родительский класс, содержит статическую информацию о товаре, название и цену.
    Добавлена инкапсуляция, оба параметра приватные.
    Добавлены методы получения параметров извне класса
    """
    
    def __init__(self, name: str, price: float) -> None:
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        """
        self.__name = name
        self.__price = price
    
    @property
    def name(self) -> str:
        """
        Метод получения названия товара.
        :return: str - название товара.
        """
        return self.__name
    
    @property
    def price(self) -> float:
        """
        Метод получения цены товара.
        :return: float - цена товара.
        """
        return self.__price


class ItemDiscountReport(ItemDiscount):
    """
    Дочерний класс, содержит метод (get_parent_data),
    отвечающий за отображение информации о товаре в одной строке.
    """
    
    def __init__(self, name: str, price: float) -> None:
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        """
        super().__init__(name, price)
    
    def get_parent_data(self) -> str:
        """
        Метод отображения информации о товаре в одной строке.
        :return: str - информация о товаре в одной строке.
        """
        return f'{self.name} - {self.price}'


if __name__ == '__main__':
    parent = ItemDiscount('ноутбук "Lenovo"', 65000.800)
    child = ItemDiscountReport(parent.name, parent.price)
    print(child.get_parent_data())
