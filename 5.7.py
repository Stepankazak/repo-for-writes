import json

with open('7.json', 'w') as fw:
    with open('7.txt', encoding='utf-8') as f:
        profit = {name.split()[0]: int(name.split()[2]) - int(name.split()[3]) for name in f}
        result = [profit, {'aver_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, fw, ensure_ascii=False, indent=4)