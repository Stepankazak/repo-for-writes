def func(a, b):
    try:
        a, b = int(a), int(b)
        test = a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return round(test , 4)

print(func(input('1 Введите число :'),input('2 Введите число :')))
