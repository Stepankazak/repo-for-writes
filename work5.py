cash = int(input('Введите выручку: '))
minus = int(input('Введите издержки: '))
plus = cash - minus
if cash > minus:
    print('Фирма отработала с прибылью')
    rentab = plus / cash * 100
    print('Рентабельность выручки составляет:', int(rentab),'%')
    people = int(input('Введите численность сотрудников фирмы: '))
    alone = cash // people
    print('Каждый сотрудник заработал фирме', alone, 'руб.')
else:
    print('Фирма отработала с убытком')



