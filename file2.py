test = list(input('Введите список: '))
list2 = 0
for i in range(int(len(test)/ 2)):
    test[list2], test[list2 + 1] = test[list2 + 1] , test[list2]
    list2 += 1
    print(test)
