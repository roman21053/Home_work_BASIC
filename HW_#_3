# 1. Define the id of next variables:
print("task #1")
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

variables = [int_a, str_b, set_c, lst_d, dict_e]

for variable in variables:
    print(f"The id for variable {variable} is: ", id(variable))
print()

# 2. Append 4 and 5 to the lst_d and define the id one more time.
print("task #2")
lst_d.append(4)
lst_d.append(5)
print(f"After append 4 and 5 the id for variable lst_d = {lst_d} is: ", id(lst_d))
print()


# 3. Define the type of each object from step 1.
print("task #3")
for variable in variables:
    print(f"The type of object {variable} is: ", type(variable))
print()


# 4*. Check the type of the objects by using isinstance.
print("task #4")
print(f"Is the data type for '{int_a}' a integer? - {isinstance(int_a, int)}")
print(f"Is the data type for '{str_b}' a string? - {isinstance(str_b, str)}")
print(f"Is the data type for '{set_c}' a set of data? - {isinstance(set_c, set)}")
print(f"Is the data type for '{lst_d}' a list? - {isinstance(lst_d, list)}")
print(f"Is the data type for '{dict_e}' a dictionary? - {isinstance(dict_e, dict)}")
print()


"""String formatting:
Replace the placeholders with a value:
"Anna has ___ apples and ___ peaches."
"""
# 5. With .format and curly braces {}
print("task #5")
apples = 10
peaches = 5

print("Anna has {} apples and {} peaches." .format(apples, peaches))
print()


# 6. By passing index numbers into the curly braces.
print("task #6")
print("Anna has {0} apples and {1} peaches." .format(apples, peaches))
print()


# 7. By using keyword arguments into the curly braces.
print("task #7")
print("Anna has {apple} apples and {peach} peaches." .format(apple=apples, peach=peaches))
print()


# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("task #8")
print("Anna has {0:^5} apples and {1:^3} peaches." .format(apples, peaches))
print()


# 9. With f-strings and variables
print("task #9")
print(f"Anna has {apples} apples and {peaches} peaches." )
print()


# 10. With % operator
print("task #10")
print("Anna has %d apples and %d peaches." % (apples, peaches))
print()


# 11*. With variable substitutions by name (hint: by using dict)
print("task #11")
fruit_dict = {'apples': apples, 'peaches': peaches}

print(f"Anna has {fruit_dict.get('apples')} apples and {fruit_dict.get('peaches')} peaches.")
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
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
print()


# 13. Convert (2) to regular for with if-else
print("task #13")
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
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
dict_comprehension_for_3 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension_for_3)
print()


# 15*. Convert (4) to dict comprehension.
print("task #15")
dict_comprehension_for_4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11) }
print(dict_comprehension_for_4)
print()


# 16. Convert (5) to regular for with if.
print("task #16")
dict_comprehension_for_5 ={}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension_for_5[x] = x**3
print(dict_comprehension_for_5)
print()

# 17*. Convert (6) to regular for with if-else.
print("task #17")
dict_comprehension_for_6 ={}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension_for_6[x] = x**3
    else:
        dict_comprehension_for_6[x] = x
print(dict_comprehension_for_6)
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

foo_lambda = lambda x, y: x if x < y else y
print("lambda x, y: x if x < y else y")
print()


# 19*. Convert (8) to regular function
print("task #19")
def foo (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print("""
def foo (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
        """)

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print("task #20")
lst_to_sort_from_min = sorted(lst_to_sort)
print(lst_to_sort_from_min)
print()

# 21. Sort lst_to_sort from max to min
print("task #21")
lst_to_sort_from_max = sorted(lst_to_sort, reverse=True)
print(lst_to_sort_from_max)
print()

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("task #22")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_by_2 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort_by_2)
print()


# 23*. Raise each list number to the corresponding number on another list:
print("task #23")
list_A = [2, 3, 4]
list_B = [5, 6, 7]

common_values = list(map(lambda number: number ** list_B[list_A.index(number)], list_A))
print(common_values)
print()


# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("task #24")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_filter = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(lst_to_sort_filter)
print()


# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("task #25")
b = range(-10, 10)
negative_numbers_from_b = list(filter(lambda x: x < 0 , b))
print(negative_numbers_from_b)
print()


# 26*. Using the filter function, find the values that are common to the two lists:
print("task #26")
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
common_values = list(filter(lambda number: number in list_2, list_1))
print(common_values)