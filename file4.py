text = input('Введите слова через пробел: ').split()
for num , i in enumerate(text, 1):
    print(num, i[:10])