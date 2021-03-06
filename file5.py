my_list = [7, 5, 3, 3, 2]
n = 0
enter = int(input('Введите число: '))
for i  in my_list:
    if enter <= i:
        n += 1
my_list.insert(n, float(enter))
print(my_list)