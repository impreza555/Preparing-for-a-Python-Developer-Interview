import os

# import psutil

# Можно сделать, чтобы поиск вёлся по всем дискам, но, для этого мне потребовался
# сторонний модуль psutil, а по теме урока у нас стандартная библиотека,
# и второй момент - по всем дискам ищет очень долго.

# генератор, итерируется по буквам дисков
# drives = (partition.device for partition in psutil.disk_partitions())
drives = ['C:\\']  # Ограничимся одним диском.)


def file_find(file_name: str) -> tuple:
    """
    Функция для поиска полного пути по имени файла.
    :param file_name: str - имя файла.
    :return: tuple - кортеж: (полный путь до файла, имя файла без расширения).
    """
    for disk in drives:
        for address, dirs, files in os.walk(disk):
            for name in files:
                if name == file_name:
                    f_path = os.path.join(address, name)
                    temp = '.'.join(name.split('.')[0:-1])
                    name_without_ext = temp if temp else name
                    return f_path, name_without_ext


if __name__ == '__main__':
    # .gitconfig я думаю, должен быть на любом компе, у тех, кто работает с гитом.
    data = file_find('.gitconfig')
    print(f'Путь: {data[0]}\nИмя файла: {data[1]}')
    # Этот файл есть только на винде.
    # data = file_find('IconCache.db')
    # print(f'Путь: {data[0]}\nИмя файла: {data[1]}')
