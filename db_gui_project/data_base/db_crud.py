import os
import sqlite3
from data_base.create_db import create_db


def connect_db(path: str) -> sqlite3.Connection:
    """
    Функция принимает путь к базе данных и возвращает объект соединения.
    Если база не существует, вызывается функция create_db, которая создаёт БД,
    а затем возвращает объект соединения.
    :param path: Путь к базе данных.
    :return: sqlite3.Connection - объект соединения.
    """
    if os.path.exists(path):
        connect = sqlite3.connect(path)
    else:
        create_db(path)
        connect = sqlite3.connect(path)
    return connect


def sql_fetch(con: sqlite3.Connection) -> list:
    """
    Функция принимает объект соединения, возвращает список имён таблиц.
    :param con: - Объект соединения.
    :return: list - список имён таблиц.
    """
    cursor = con.cursor()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    table_list = [item[0] for item in cursor.fetchall()]
    return table_list


def names_of_table_columns(con: sqlite3.Connection, table_name: str) -> list:
    """
    Функция принимает объект соединения и имя таблицы, возвращает список имён столбцов таблицы.
    :param con: - Объект соединения.
    :param table_name: str - имя таблицы
    :return: list - список имён столбцов таблицы.
    """
    cursor = con.cursor()
    info = cursor.execute(f'PRAGMA table_info({table_name})')
    columns_list = [item[1] for item in info.fetchall()]
    return columns_list


def read(con: sqlite3.Connection, table_name: str) -> list:
    """
    Функция принимает объект соединения и имя таблицы, возвращает список данных таблицы.
    :param con: - Объект соединения.
    :param table_name: str - имя таблицы
    :return: list - список данных таблицы.
    """
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    data = list(cursor.fetchall()[0])
    return [data]


if __name__ == '__main__':
    path_db = 'goods_db.sqlite3'
    connection = connect_db(path_db)
    print(sql_fetch(connection))
    print(names_of_table_columns(connection, 'goods'))
    print(read(connection, 'goods'))
    connection.close()
    temp = ['categories', 'units', 'positions', 'goods', 'sqlite_sequence', 'employees', 'vendors']
