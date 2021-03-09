def inform(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
new_day = input('Введите день рождения: ')
city = input('Введите город: ')
mail = input('Введите почту: ')
number_ph = input('Введите номер телефона: ')

print(inform(
    name = name,
    surname = surname,
    new_day = new_day,
    city = city,
    mail = mail,
    number_ph = number_ph
))
