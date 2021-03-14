from itertools import count, cycle
print('Программа целых чисел')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повтора элементов списка')

new_list = input('Введите список через пробел').split()
iter = cycle(new_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()
