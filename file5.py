my_list = [7, 5, 3, 3, 2]

enter = input('Введите число: ')
for i  in range(0, 10 ):
    if enter in my_list:
        my_list.append(enter)
        print(my_list)
        # тестовый вариант. за выполненное задание не считать