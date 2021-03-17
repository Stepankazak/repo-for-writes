with open('2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())}']
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')