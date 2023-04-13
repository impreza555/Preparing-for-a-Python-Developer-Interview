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


class ItemDiscountReport1(ItemDiscount):
    """
    Дочерний класс №1 демонстрирующий возможности полиморфизма.
    """
    
    def __init__(self, name: str, price: float):
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        """
        super().__init__(name, price)
    
    def get_info(self) -> str:
        """
        Метод вывода названия товара.
        :return: str - название товара.
        """
        return f'{self.__class__.__name__}: {self.name}'


class ItemDiscountReport2(ItemDiscount):
    """
        Дочерний класс №2 демонстрирующий возможности полиморфизма.
        """
    
    def __init__(self, name: str, price: float):
        """
        Конструктор класса.
        :param name: str - название товара.
        :param price: float - цена товара.
        """
        super().__init__(name, price)
    
    def get_info(self) -> str:
        """
        Метод вывода названия товара.
        :return: str - название товара.
        """
        return f'{self.__class__.__name__}: {self.price}'


def obj_info(obj: object) -> None:
    """
    Функция, принимает объект, и вызывает его метод.
    :param obj: object - объект.
    :return: None
    """
    print(f'{obj_info.__name__}: {obj.get_info()}')


if __name__ == '__main__':
    parent = ItemDiscount('ноутбук "Lenovo"', 65000.800)
    print(f'parent: {parent.name}, {parent.price}')
    child1 = ItemDiscountReport1(parent.name, parent.price)
    child2 = ItemDiscountReport2(parent.name, parent.price)
    
    # Способ 1: вызов метода экземпляра класса
    print(f'child: {child1.get_info()}')
    print(f'child: {child2.get_info()}')
    
    # Способ 2: обращение к методу экземпляра с помощью функции
    obj_info(child1)
    obj_info(child2)
    
    # Способ 3: получение и вызов метода экземпляра класса с помощью getattr()
    print('getattr', getattr(child1, 'get_info')())
    print('getattr', getattr(child2, 'get_info')())
