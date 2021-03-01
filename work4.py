number = int(input('Введите целое положительное число: '))
big = number % 10
number = number // 10
while number > 10:
    if number % 10 > big:
        big = number % 10
    number = number // 10

print(big)
print('Конец программы')


