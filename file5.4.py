rus_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре' }
with open('4.txt', 'w', encoding='utf-8') as nf, open('4m.txt', 'r', encoding='utf-8') as mf:
    nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))