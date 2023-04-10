import os


def print_directory_contents(s_path: str) -> None:
	"""
	Функция - аналог функции os.walk. Принимает имя каталога и распечатывает его содержимое
	в виде «путь и имя файла», а также любые другие
	файлы во вложенных каталогах, (рекурсивно вызывая себя).
	:param s_path: путь до каталога
	:return: None
	"""
	with os.scandir(s_path) as dir_path:
		for entry in dir_path:
			if entry.is_file():
				print(entry.path)
			elif entry.is_dir():
				print(f'\033[1m\033[30m\033[47m{entry.path}\033[0m')
				print_directory_contents(entry.path)


if __name__ == '__main__':
	# print_directory_contents(r'F:\Music')
	print_directory_contents(r'.')
