import time


def randomizer(seed: int = time.time_ns()) -> object:
	"""
	Функция генерирует случайные числа в диапазоне [0; 1].
	В основе работы лежит Линейный конгруэнтный метод.
	:param seed: int - начальное значение
	:return: float - случайное число
	"""
	module = 2 ** 31 - 1
	increment = 0
	initializer = 48271
	while True:
		temp = (seed * initializer + increment) % module
		initializer = temp
		rand_float = round((temp % 1000 / 1000), 2)
		yield rand_float


def random_list(start: int, end: int, generator: object) -> list:
	"""
	Функция создаёт список положительных целых случайных чисел
	в диапазоне (start; end), включительно.
	:param start: int - начальное значение
	:param end: int - конечное значение
	:param generator: object - генератор случайных чисел
	:return: list - список случайных чисел
	"""
	return [int((start + (end - start)) * next(generator)) for i in range(end - start + 1)]


def random_dict(start: int, end: int, generator: object) -> dict:
	"""
	Функция создаёт словарь положительных целых случайных чисел
	в диапазоне (start; end), включительно, по шаблону {“elem_<номер_элемента>”: elem}.
	:param start: int - начальное значение
	:param end: int - конечное значение
	:param generator: object - генератор случайных чисел
	:return: dict - список случайных чисел
	"""
	return {f"elem_{i}": int((start + (end - start)) * next(generator)) for i in range(end - start + 1)}


if __name__ == "__main__":
	first = 0
	last = 20
	gen = randomizer()
	print(type(gen))
	print(random_list(first, last, gen))
	print(random_dict(first, last, gen))
