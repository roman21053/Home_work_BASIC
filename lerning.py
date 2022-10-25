def myfunc(lst_1, lst_2):
    temp_list = []
    for num in range(len(lst_1)):
        for num2 in range(len(lst_1)):
            if lst_1[num] == lst_2[num2]:
                temp_list.append(lst_1[num])
            else:
                pass
    return temp_list


list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 9]
print(myfunc(list_1, list_2))