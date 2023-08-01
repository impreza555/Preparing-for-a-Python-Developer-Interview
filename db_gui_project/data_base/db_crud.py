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


def names_of_db_tables(con: sqlite3.Connection) -> list:
    """
    Функция принимает объект соединения, возвращает список имён таблиц.
    :param con: - Объект соединения.
    :return: List - список имён таблиц.
    """
    cursor = con.cursor()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    table_list = [item[0] for item in cursor.fetchall()]
    return table_list


def names_of_table_columns(con: sqlite3.Connection, table_name: str) -> dict:
    """
    Функция принимает объект соединения и имя таблицы, возвращает список имён столбцов таблицы.
    :param con: - Объект соединения.
    :param table_name: Str - имя таблицы
    :return: dict - словарь, где ключи - имена столбцов таблицы, значения - является ли столбец
    первичным ключом, и используется ли авто инкремент
    """
    cursor = con.cursor()
    info = cursor.execute(f'PRAGMA table_info({table_name})')
    columns_dict = {}
    for item in info:
        columns_dict[item[1]] = [True if item[-1] == 1 else False, True if item[2] == 'INTEGER' else False]
    return columns_dict


def table_relations(con: sqlite3.Connection, table_name: str) -> list:
    """
    Функция принимает объект соединения, и имя таблицы, возвращает список,
    представляющий данные об отношениях таблицы к другим таблицам.
    :param con: - Объект соединения.
    :param table_name: Str - имя таблицы
    :return: list - список отношений таблицы к другим таблицам.
    """
    relation_list = []
    cursor = con.cursor()
    info = cursor.execute(f'PRAGMA foreign_key_list({table_name})')
    for item in info:
        temp_dict = {'rel_table': item[2], 'fk': item[3], 'rel_table_pk': item[4]}
        relation_list.append(temp_dict)
    return relation_list


def read(con: sqlite3.Connection, table_name: str) -> list:
    """
    Функция принимает объект соединения и имя таблицы, возвращает список данных таблицы.
    :param con: - Объект соединения.
    :param table_name: Str - имя таблицы
    :return: list - список данных таблицы
    """
    query = f'SELECT * FROM {table_name}'
    cursor = con.cursor()
    cursor.execute(query)
    data = list([list(row) for row in cursor.fetchall()])
    return data


def insert(con: sqlite3.Connection, table_name: str, columns: list, data: list) -> None:
    """
    Функция принимает объект соединения и имя таблицы, список столбцов и список данных для вставки
    и вставляет данные в таблицу.
    :param con: - Объект соединения.
    :param table_name: Str - имя таблицы
    :param columns: List - имена столбцов
    :param data: List - список данных для вставки.
    :return: None
    """
    plug = ",".join(['?' for _ in range(len(columns))])
    query = f'INSERT INTO {table_name}({", ".join(columns)}) VALUES ({plug})'
    cursor = con.cursor()
    cursor.execute(query, data)
    con.commit()


def delete(con: sqlite3.Connection, table_name: str, column_name: str, value: str) -> None:
    """
    Функция принимает объект соединения и имя таблицы, имя столбца и значение для удаления
    :param con: - Объект соединения.
    :param table_name: Str - имя таблицы
    :param column_name: Str - имя столбца
    :param value: Str - значение для удаления
    :return: None
    """
    query = f'DELETE FROM {table_name} WHERE {column_name} = ?'
    cursor = con.cursor()
    cursor.execute(query, (value,))
    con.commit()


if __name__ == '__main__':
    path_db = 'goods_db.sqlite3'
    connection = connect_db(path_db)
    # print(names_of_db_tables(connection))
    # print(names_of_table_columns(connection, 'categories'))
    # print(read(connection, 'goods', 'good_name'))
    # print(table_relations(connection, 'goods'))
    # insert(connection, 'goods', ['good_name', 'good_unit', 'good_cat'],
    #        ['абрикосы', 'килограммы', 'фрукты'])
    connection.close()
