import PySimpleGUI as sg
from data_base.db_crud import *

path_db = ''
sg.theme('LightGreen')

# Макет меню
menu_default = [
    ['Таблицы', []],
    ['Справка', 'О программе'],
]
# Макет основного окна
layout = [
    [sg.Menu(menu_default, key='-MENU-', tearoff=False)],
    [sg.Frame(
        'Выберите файл базы данных',
        [[
            sg.Input(
                key="-IN-",
                change_submits=True,
                expand_x=True,
                readonly=True,
                default_text='Путь к файлу БД...'
            ),
            sg.FileBrowse(
                button_text='Открыть',
                key="-IN-",
                file_types=(("ALL Files", "*.*"),),
                enable_events=True,
            )
        ]],
        key='-FRAME-',
        expand_x=True,
        border_width=3
    )],
    [sg.Frame(
        'Таблица',
        [[]],
        key='-TABLE-',
        expand_x=True,
        expand_y=True,
        border_width=3,
    )],
    [
        sg.Push(),
        sg.Button('Добавить', key='-ADD-', visible=False),
        sg.Button('Удалить', key='-DELL-', visible=False, disabled=True),
    ],
]


def make_win1() -> sg.Window:
    """
    Функция создаёт окно для работы с базой данных
    :return:  Объект окна
    """
    global layout
    window = sg.Window(
        "Работа с базой данных",
        layout,
        default_element_size=(12, 1),
        auto_size_text=False,
        auto_size_buttons=True,
        size=(600, 400),
        finalize=True
    )
    return window


def make_win2(add_layout) -> sg.Window:
    """
    Функция создаёт окно для добавления данных в таблицу.
    :param add_layout: List - макет окна.
    :return: Объект окна
    """
    window = sg.Window(
        "Добавить",
        add_layout,
        default_element_size=(12, 1),
        auto_size_text=False,
        auto_size_buttons=True,
        finalize=True
    )
    return window


current_table = ''  # Текущая таблица
tables_data = {}  # Словарь данных таблиц
table_list = []  # Список таблиц


def table_data_maker(con: sqlite3.Connection, tab_list: list) -> None:
    """
    Функция создаёт словарь данных таблиц
    :param con: - Объект соединения
    :param tab_list: List - Список таблиц
    :return: None
    """
    global tables_data
    for table in tab_list:
        tables_data[table] = {
            'headings': names_of_table_columns(con, table),
            'data': read(con, table)
        }


def main() -> None:
    """
    Функция запускает программу
    :return: None
    """
    global current_table, tables_data, table_list, path_db
    window1, window2 = make_win1(), None
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:
                window2 = None
            elif window == window1:
                break
        elif event == 'О программе':
            sg.popup(
                'About this program',
                'Version 1.0',
                'Made with PySimpleGUI by impreza555'
            )
        elif event == '-IN-':
            path_db = values['-IN-']
            conn = connect_db(path_db)
            table_list = names_of_db_tables(conn)
            if 'sqlite_sequence' in table_list:
                table_list.remove('sqlite_sequence')
            table_data_maker(conn, table_list)
            conn.close()
            menu_default[0][1] = table_list
            window['-MENU-'].update(menu_default)
            tab_layout = []
            for table in table_list:
                tab_layout.append([
                    sg.pin(sg.Table(
                        headings=list(tables_data[table]['headings']),
                        values=tables_data[table]['data'],
                        expand_x=True,
                        expand_y=True,
                        key=f'-{table}-',
                        visible=False,
                        auto_size_columns=True,
                        vertical_scroll_only=False,
                    ))
                ])
            window.extend_layout(window['-TABLE-'], tab_layout)
            window.refresh()
        elif event in menu_default[0][1]:
            for table in menu_default[0][1]:
                if table == event:
                    window[f'-{table}-'].update(visible=True)
                    window['-ADD-'].update(visible=True)
                    window['-DELL-'].update(visible=True)
                    current_table = table
                    window['-TABLE-'].update(f'Таблица: {table}')
                else:
                    window[f'-{table}-'].update(visible=False)
        elif event == '-ADD-' and not window2:
            conn = connect_db(path_db)
            relation_tab_data = table_relations(conn, current_table)
            conn.close()
            add_layout = []
            for col_name in tables_data[current_table]['headings'].keys():
                if tables_data[current_table]['headings'][col_name] == [True, True]:
                    continue
                elif col_name in [el['fk'] for el in relation_tab_data]:
                    for el in relation_tab_data:
                        if el['fk'] == col_name:
                            combo_values = [
                                _[list(tables_data[el['rel_table']]['headings']).index(el['rel_table_pk'])]
                                for _ in tables_data[el['rel_table']]['data']
                            ]
                            add_layout.append([
                                sg.Text(f'{col_name}'),
                                sg.Combo(values=combo_values, readonly=True, key=f'-{col_name}-', size=(20, 1)),
                            ])
                else:
                    add_layout.append([
                        sg.Text(f'{col_name}'),
                        sg.InputText(key=f'-{col_name}-', size=(20, 1)),
                    ])
            add_layout.append([[sg.Push(), sg.Button('Добавить', key='-AD_ROW-')]])
            window2 = make_win2(add_layout)
        elif event == '-AD_ROW-' and window2:
            conn = connect_db(path_db)
            columns = list(map(lambda x: x.replace("-", ""), list(values)))
            row_values = list(values.values())
            try:
                insert(conn, current_table, columns, row_values)
                table_data_maker(conn, table_list)
            except sqlite3.Error as err:
                sg.popup('Ошибка', f'{err}')
            finally:
                conn.close()
            window.close()
            if window == window2:
                window2 = None
            elif window == window1:
                break
            window1[f'-{current_table}-'].update(values=tables_data[current_table]['data'])
    window.close()


if __name__ == '__main__':
    main()
