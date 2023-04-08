def bank_deposit(deposit_amount: float, period: int) -> float | None:
	"""
	Функция - банковский депозит. Принимает сумму и срок вклада.
	Срок вклада 6, 12 и 24 месяцев.
	В зависимости от суммы и срока вклада определяется процентная ставка.
	Возвращает сумму вклада на конец указанного срока.
	:param deposit_amount: float - сумма вклада.
	:param period: int - срок вклада.
	:return: float - сумма вклада на конец срока.
	"""
	deposit1: dict[str | int, int | float] = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
	deposit2: dict[str | int, int | float] = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
	deposit3: dict[str | int, int | float] = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
	selected_deposit = None
	if deposit_amount in range(deposit1['begin_sum'], deposit1['end_sum']):
		selected_deposit = deposit1
	elif deposit_amount in range(deposit2['begin_sum'], deposit2['end_sum']):
		selected_deposit = deposit2
	elif deposit_amount in range(deposit3['begin_sum'], deposit3['end_sum']):
		selected_deposit = deposit3
	else:
		print('Неподходящая сумма вклада')
		return
	if period in (6, 12, 24):
		return deposit_amount + deposit_amount * selected_deposit[period] * period / 12
	else:
		print('Неподходящий срок вклада')
		return


if __name__ == '__main__':
	print(bank_deposit(5000, 6))
	print(bank_deposit(65000, 12))
	print(bank_deposit(356000, 24))
