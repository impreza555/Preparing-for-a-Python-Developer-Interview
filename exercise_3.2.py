try:
    num = float(input('Введите число: ').replace(',', '.'))
except ValueError:
    print('Вы ввели не число')
else:
    integer = int(num)
    fractal = str(float(num))
    fractal = int(fractal[fractal.find('.') + 1:])
    if not fractal:
        print("Целое")
    else:
        print("Дробное")
        print(integer == fractal)
