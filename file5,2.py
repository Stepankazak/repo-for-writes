def sum_func():
    a = 0
    while True:
        text = input('Введите число, или q для выхода: ').split()
        for i in text:
            if i == 'q':
                return a
            else:
                try:
                    a += int(i)
                except ValueError:
                    print('q для выхода')
        print(f'Сумма чисел = {a}')
print(sum_func())