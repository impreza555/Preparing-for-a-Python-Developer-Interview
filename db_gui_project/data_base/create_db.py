import sqlite3


def create_db(path_db: str) -> None:
    """
    Функция создает базу данных и таблицы в базе данных.
    :param path_db: Путь к базе данных.
    :return: None
    """
    connection = sqlite3.connect(path_db)
    cursor = connection.cursor()
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS categories
        (category_name VARCHAR(100) NOT NULL PRIMARY KEY,
        category_description TEXT NOT NULL);

        CREATE TABLE IF NOT EXISTS units
        (unit VARCHAR(100) NOT NULL PRIMARY KEY);

        CREATE TABLE IF NOT EXISTS positions
        (position VARCHAR(100) NOT NULL PRIMARY KEY);
        

        CREATE TABLE IF NOT EXISTS goods
        (good_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        good_name VARCHAR(100) NOT NULL,
        good_unit VARCHAR(100) NOT NULL,
        good_cat VARCHAR(100) NOT NULL,
        FOREIGN KEY (good_unit) REFERENCES units (unit) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (good_cat) REFERENCES categories (category_name) ON UPDATE CASCADE ON DELETE CASCADE);
        
        CREATE TABLE IF NOT EXISTS employees
        (employee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        employee_fio VARCHAR(255) NOT NULL,
        employee_position TEXT NOT NULL,
        FOREIGN KEY (employee_position) REFERENCES positions (position) ON UPDATE CASCADE ON DELETE CASCADE);
        
        CREATE TABLE IF NOT EXISTS vendors
        (vendor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        vendor_name VARCHAR(100) NOT NULL,
        vendor_ownerchipform VARCHAR(100) NOT NULL,
        vendor_address  VARCHAR(255) NOT NULL,
        vendor_phone VARCHAR(16) NOT NULL,
        vendor_email VARCHAR(255) NOT NULL);
        PRAGMA foreign_keys = ON;
        """
    )
    connection.commit()
    connection.close()


if __name__ == '__main__':
    db_path = 'goods_db.sqlite3'
    create_db(db_path)
