from sys import argv

def salary():
    try:
        time , text , result = map(float, argv[1:])
        print(f"Salary - {time * text + result}")
    except ValueError:
        print('Повторите ввод')

salary()