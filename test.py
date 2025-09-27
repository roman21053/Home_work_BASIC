lst_to_sort = [9, 11, 3, 0, 5, 6, 7]

new_sort = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))

print(new_sort)
print()