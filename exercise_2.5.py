class ItemDiscount:
    """
    Родительский класс, содержит статическую информацию о товаре, название и цену.
    Добавлена инкапсуляция, оба параметра приватные.
    Добавлены методы получения параметров извне класса
    Так же добавлены методы переустановки значений параметров.
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
    
    @name.setter
    def name(self, name: str) -> None:
        """
        Метод изменения названия товара.
        :param name: str - новое название товара.
        """
        self.__name = name
    
    @price.setter
    def price(self, price: float) -> None:
        """
        Метод изменения цены товара.
        :param price: float - новая цена товара.
        """
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    """
    Дочерний класс, содержит метод (get_parent_data),
    отвечающий за отображение информации о товаре в одной строке.
    Добавлен параметр discount, который передается в качестве аргумента в дочерний класс.
    """
    
    def __init__(self, name: str, price: float, discount: int = 0) -> None:
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        :param discount: int - скидка в процентах.
        """
        super().__init__(name, price)
        self.discount = discount
    
    def __str__(self) -> str:
        """
        Метод отображения информации о товаре в строковом виде.
        :return: str - информация о товаре в строке.
        """
        ending = f' (цена со скидкой {self.discount}%)' if self.discount > 0 else f''
        return f'{self.name} - {round(self.price - self.price * (self.discount / 100), 2)}{ending}'
    
    def get_parent_data(self) -> str:
        """
        Метод отображения информации о товаре в одной строке.
        :return: str - информация о товаре в одной строке.
        """
        return f'{self.name} - {self.price}'


if __name__ == '__main__':
    parent = ItemDiscount('ноутбук "Lenovo"', 65000.800)
    print(f'parent: {parent.name}, {parent.price}')
    parent.name, parent.price = 'телевизор "Samsung"', 35000.300
    print(f'parent: {parent.name}, {parent.price}')
    child = ItemDiscountReport(parent.name, parent.price, 30)
    print(f'child: {child.get_parent_data()}')
    print(f'child: {str(child)}')
