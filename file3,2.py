def my_func(list1, list2, list3):
    all_list = [list1, list2, list3]
    return sum(sorted(all_list)[1:])

print(my_func(15, 18, 16))