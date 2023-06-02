import PySimpleGUI as sg
from data_base.db_crud import sql_fetch, connect_db, names_of_table_columns, read

path_db = ''
sg.theme('LightGreen')

menu_def = [
    ['Таблицы', []],
    ['Справка', 'О программе'],
]

layout = [
    [sg.Menu(menu_def, key='-MENU-', tearoff=False)],
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
]

window = sg.Window(
    "Работа с базой данных",
    layout,
    default_element_size=(12, 1),
    auto_size_text=False,
    auto_size_buttons=True,
    size=(600, 400),
)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == 'О программе':
        sg.popup(
            'About this program',
            'Version 1.0',
            'Made in PySimpleGUI by impreza555'
        )
    elif event == '-IN-':
        path_db = values['-IN-']
        print(path_db)
        connection = connect_db(path_db)
        table_list = sql_fetch(connection)
        menu_def[0][1] = table_list
        window['-MENU-'].update(menu_def)
        tab_layout = []
        for table in table_list:
            tab_layout.append([
                sg.pin(sg.Table(
                    values=read(connection, table),
                    headings=names_of_table_columns(connection, table),
                    expand_x=True,
                    expand_y=True,
                    key=f'-{table}-',
                    visible=False,
                    auto_size_columns=True,
                    vertical_scroll_only=False
                ))
            ])
        window.extend_layout(window['-TABLE-'], tab_layout)
        window.refresh()
        connection.close()
    elif event in menu_def[0][1]:
        for table in menu_def[0][1]:
            if table == event:
                window[f'-{table}-'].update(visible=True)
                window['-TABLE-'].update(f'Таблица: {table}')
            else:
                window[f'-{table}-'].update(visible=False)
