from random import randint

list = [randint(-10, 10) for _ in range(20)]
new_list = [el for el in list if list.count(el) == 1]
print(f'Начальный список\n{list}\n Список без повторений\n{new_list}')