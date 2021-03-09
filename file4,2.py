def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Ошибка x больше 0, a y меньше 0'
        else:
            result = 1
            for i in range(abs(y)):
                result *= 1 / x
            return f'результат вычисления: {round(result, 6)}'
    except ValueError:
        return "Введите числа!"

print(my_func(5, -5))