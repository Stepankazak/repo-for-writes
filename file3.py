ear = {
    'Лето' :(6, 7, 8),
    'Зима': (12, 1, 2),
    'Осень': (9, 10, 11),
    'Весна': (3, 4, 5)
      }

text = int(input('Введите номер месяца: '))
for key in ear.keys():
    if text in ear[key]:
        print(key)


