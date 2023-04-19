from random import randint
from typing import List, Any
from string import ascii_lowercase


def custom_zip_dict(keys: List[int | float | str | tuple | bool], values: List[Any]) -> dict | None:
    """
    Функция принимает два списка и создаёт словарь с ключами из первого списка и значениями из второго списка.
    Если ключу не хватает значения, в словаре для него сохраняется значение None.
    Значения, которым не хватило ключей, отбрасываются.
    :param keys: list - список ключей.
    :param values: list - список значений.
    :return: dict - итоговый словарь или None
    """
    if any([type(x) in (list, dict, set, bytearray) for x in keys]):
        print('Ключи словаря не могут быть мутабельными объектами')
        return
    dict_ = {}
    for idx, key in enumerate(keys):
        if idx > len(values) - 1:
            dict_[key] = None
        else:
            dict_[key] = values[idx]
    return dict_


if __name__ == '__main__':
    list1 = [i for i in range(randint(1, 10))]
    list2 = [ascii_lowercase[i] for i in range(randint(1, 10))]
    print(list1)
    print(list2)
    print(custom_zip_dict(list1, list2))
