my_list = [15, 6, 2, 3, 1, 7, 5, 4, 10]
status = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(status)