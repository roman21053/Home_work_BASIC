# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("Task #3")


gener_square_numbers = (f"{index} ** 2 = {index**2}" for index in range(11))
print(type(gener_square_numbers))
for i in gener_square_numbers:
    print(i)
