mu_dict = {}
with open('6.txt', encoding='utf-8') as f:
    for line in f:
        name, status = line.split(':')
        name_sum = sum(map(int, "".join([i for i in status if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mu_dict[name] = name_sum
    print(f'{mu_dict}')