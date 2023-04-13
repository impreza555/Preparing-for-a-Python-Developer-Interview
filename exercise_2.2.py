class ItemDiscount:
    """
    Родительский класс, содержит статическую информацию о товаре, название и цену.
    Добавлена инкапсуляция, оба параметра приватные.
    """
    
    def __init__(self, name: str, price: float) -> None:
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        """
        self.__name = name
        self.__price = price


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
    child = ItemDiscountReport(parent.name,
                               parent.price)  # Здесь генерируется ошибка, т.к. параметры родительского класса приватные
    print(child.get_parent_data())
