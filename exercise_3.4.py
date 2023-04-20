import os
from random import choice, randint
from string import ascii_letters
from os.path import join, exists


def text_file_creation(file_name: str) -> None:
    """
    Функция создает текстовый файл. Если файл с таким именем существует, выводим соответствующее сообщение.
    Далее генерируются два списка с текстовой и числовой информацией. Затем с помощью функции zip() содержимое
    этих списков преобразуются в строку и записываются в файл, где каждая строка содержит текстовое и числовое значение.
    :param file_name: str - имя файла.
    :return: None
    """
    path = os.getcwd()
    file = join(path, file_name)
    if exists(file):
        print('Файл с таким именем уже существует!!!')
    text_list = [''.join([choice(ascii_letters) for _ in range(5)]) for _ in range(21)]
    num_lst = [randint(100, 1000) for _ in range(21)]
    with open(file, 'w', encoding='utf-8') as f:
        for _ in zip(text_list, num_lst):
            print(f'{_[0]} - {_[1]}', file=f)
    text_file_read(file)


def text_file_read(file_name: str) -> None:
    """
    Функция читает содержимое файла и построчно выводит его на экран.
    :param file_name: str - имя файла.
    :return: None
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    text_file_creation('test.txt')
