# 1. Define the id of next variables:
print("task #1")

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

for_id = {'int_a': int_a, 'str_b': str_b, 'set_c': set_c, 'lst_d': lst_d, 'dict_e': dict_e}
for elem in for_id:
    print(f'id for {elem} - {id(for_id[elem])}')
print()

# 2. Append 4 and 5 to the lst_d and define the id one more time.
print("task #2")

lst_d.append(4)
lst_d.append(5)
print(lst_d)
print()

# 3. Define the type of each object from step 1.
print("task #3")

for elem in for_id:
    print(f'type for {elem} - {type(for_id[elem])}')
print()

# 4*. Check the type of the objects by using isinstance.
print("task #4")

for elem in for_id:
    r = type(for_id[elem])
    print(f'is type for {elem} {r} - {isinstance((for_id[elem]), r)}')
print()

"""String formatting:
Replace the placeholders with a value:
"Anna has ___ apples and ___ peaches."
"""
# 5. With .format and curly braces {}
print("task #5")

apples = 5
peaches = 3

phrase = 'Anna has {} apples and {} peaches.'.format(apples, peaches)

print(phrase)
print()

# 6. By passing index numbers into the curly braces.
print("task #6")

phrase = 'Anna has {0} apples and {1} peaches.'.format(apples, peaches)

print(phrase)
print()

# 7. By using keyword arguments into the curly braces.
print("task #7")

phrase = 'Anna has {apples} apples and {peaches} peaches.'.format(apples=apples, peaches=peaches)

print(phrase)
print()

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("task #8")

phrase = 'Anna has {0:^5} apples and {1:^3} peaches.'.format(apples, peaches)

print(phrase)
print()

# 9. With f-strings and variables
print("task #9")

phrase = f'Anna has {apples} apples and {peaches} peaches.'
print(phrase)
print()

# 10. With % operator
print("task #10")

phrase = 'Anna has %d apples and %d peaches.' %(apples, peaches)

print(phrase)
print()

# 11*. With variable substitutions by name (hint: by using dict)
print("task #11")

varieb = {'apples': 5, 'peaches': 3}

phrase = f'Anna has {varieb['apples']} apples and {varieb['peaches']} peaches.'
print(phrase)
print()

""" Comprehensions:
(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

(2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
"""

# 12. Convert (1) to list comprehension
print("task #12")
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
print()

# 13. Convert (2) to regular for with if-else
print("task #13")

list_comprehension = []

for num in range(10):
    if num % 2 == 1:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)

print(list_comprehension)
print()

"""(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

(5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

(6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
"""

# 14. Convert (3) to dict comprehension.
print("task #14")

d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}

print(d)
print()


# 15*. Convert (4) to dict comprehension.
print("task #15")

d = {num: num ** 2 if num % 2 == 1 else int(num // 0.5) for num in range(1, 11)}

print(d)
print()


# 16. Convert (5) to regular for with if.
print("task #16")

dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension.update({x: x**3})

print(dict_comprehension)
print()


# 17*. Convert (6) to regular for with if-else.
print("task #17")

dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension.update({x: x**3})
    else:
        dict_comprehension.update({x: x})

print(dict_comprehension)
print()

"""Lambda:

(7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

(8)
foo = lambda x, y, z: z if y < x and x > z else y
"""

# 18. Convert (7) to lambda function
print("task #18")

foo = lambda x, y: x if x < y else y

print('the smaller number is',foo(1, 2))
print()

# 19*. Convert (8) to regular function
print("task #19")

def foo (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print('our number is',foo(1, 2, 3))
print()

# 20. Sort lst_to_sort from min to max
print("task #20")

lst_to_sort = [9, 11, 3, 0, 5, 6, 7, 8]
lst_to_sort = sorted(lst_to_sort)

print(lst_to_sort)
print()

# 21. Sort lst_to_sort from max to min
print("task #21")

lst_to_sort = sorted(lst_to_sort, reverse=True)

print(lst_to_sort)
print()

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("task #22")

lst_to_sort_update = list(map(lambda elem: elem * 2, lst_to_sort))
print(lst_to_sort_update)
print()

# 23*. Raise each list number to the corresponding number on another list:
print("task #23")
another_list = [1, 2, 4, 6, 7, 3, 5, 7]
ind = 0
lst_to_sort_sum = []

for elem in another_list:
    if another_list.index(elem) == 0:
        sum = elem + lst_to_sort[ind]
        lst_to_sort_sum.append(sum)
    else:    
        ind += 1
        sum = elem + lst_to_sort[ind]
        lst_to_sort_sum.append(sum)

print(lst_to_sort_sum)
print()

print('second way')

lst_to_sort_sum = [x + y for x, y in zip(lst_to_sort, another_list)]

print(lst_to_sort_sum)
print()

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("task #24")

new_sort = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))

print(new_sort)
print()

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("task #25")

b = range(-10, 10)
negative_num = list(filter(lambda num: num < 0, b))

print(negative_num)
print()

# 26*. Using the filter function, find the values that are common to the two lists:
print("task #26")

common_val = list(filter(lambda val: val in another_list, lst_to_sort))
print(f'values that are common to the two lists - {sorted(common_val)}')
print()
