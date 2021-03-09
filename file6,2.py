def func_param(select):
    list1 = 'qwertyuiopasdfghjklzxcvbnm'
    return select.title() if not set(select).difference(list1) else False

words = input('Введите строку из слов через пробел ').split()
for i in words:
    result = func_param(i)
    if result:
        print(func_param(i), ' ')
