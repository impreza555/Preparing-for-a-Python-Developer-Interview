import os
import re
from random import choice, randint
from string import ascii_letters
from os.path import join, exists


def text_file_creation(file_name: str, substr: str, new_str: str) -> None:
    """
    Функция создает текстовый файл. Если файл с таким именем существует, выводим соответствующее сообщение.
    Далее генерируются два списка с текстовой и числовой информацией. Затем с помощью функции zip() содержимое
    этих списков преобразуются в строку и записываются в файл, где каждая строка содержит текстовое и числовое значение.
    :param file_name: str - имя файла.
    :param substr: str - подстрока для поиска.
    :param new_str: str - новая строка для замены.
    :return: None
    """
    path = os.getcwd()
    file = join(path, file_name)
    if exists(file):
        print('Файл с таким именем уже существует!!!')
    text_list = ['example' + str(randint(100, 999)) if choice([0, 1]) else ''.join(
        [choice(ascii_letters) for _ in range(5)]) for _ in range(21)]
    num_lst = [randint(100, 1000) for _ in range(21)]
    with open(file, 'w', encoding='utf-8') as f:
        for _ in zip(text_list, num_lst):
            if choice([0, 1]):
                print(f' {_[0]}{_[1]} ', file=f)
            else:
                print(f'{_[1]}{_[0]}', file=f)
    text_file_read(file, substr, new_str)


def text_file_read(file_name: str, substring: str, new_string: str) -> None:
    """
    Функция читает содержимое файла и построчно выводит его на экран.
    Так же осуществляет поиск вхождения подстроки в содержимое файла,
    замену найденной подстроки на новое значение и вывод всех подстрок,
    состоящих из букв и цифр и имеющих пробелы только в начале и конце — например.
    :param file_name: str - имя файла.
    :param substring: str - подстрока для поиска.
    :param new_string: str - новая строка для замены.
    :return: None
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    pattern = f'\w*{substring}\w*'
    print(text, ('*' * 40), sep='\n')
    first = re.search(pattern, text)
    print(f'Первое вхождение: {first.group(0)}')
    second = re.findall(pattern, text)
    print(f'Все вхождения: {second}', ('*' * 40), sep='\n')
    result = re.sub(pattern, new_string, text)
    print(f'Замена всех найденных подстрок на новое значение:', result, sep='\n')
    print(f'Вывод всех подстрок, состоящих из букв и\n'
          f'цифр и имеющих пробелы только в начале и конце:')
    for row in result.split('\n'):
        if row.startswith(' ') and row.endswith(' '):
            print(row)


if __name__ == '__main__':
    text_file_creation('test.txt', 'example', 'hello')
