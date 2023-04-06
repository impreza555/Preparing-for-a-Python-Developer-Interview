from typing import Callable

format_to_sting: Callable[[list], str] = lambda list_: "\t".join(map(str, list_))


def multiplication_table(a: int, b: int) -> None:
	"""
	Функция реализует вывод таблицы умножения размерностью AｘB.
	:param a: int - Верхняя граница диапазона первых множителей от 1 до a, включая a
	:param b: int - Верхняя граница диапазона вторых множителей от 1 до b, включая b
	:return: None
	"""
	try:
		for i in range(1, a + 1):
			print(format_to_sting([i * j for j in range(1, b + 1)]))
	except TypeError as e:
		print(e)


if __name__ == "__main__":
	multiplication_table(9, 9)
