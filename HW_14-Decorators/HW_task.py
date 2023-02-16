print("   1. double_result")

# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def inner(*args):
        return func(*args) * 2
    return  inner


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20

print()
print("   2. only_odd_parameters")
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    def wrapper(*args):
        for num in args:
            if num % 2 == 0:
                return "Please use only odd numbers!"
        return func(*args)
    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e

print(multiply(1, 2, 3, 4, 5))


print()
print('   3.* logged')
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    # log function arguments and its return value
    def wrapper(*args, **kwargs):
        arguments_log = f'Function: {func.__name__}. with arguments {args} and value {kwargs}'
        val_func = func(*args, **kwargs)

        with open('logs/log.log', 'a') as file:
            file.write(f'{arguments_log} \nfunction return value: {val_func}\n\n')

        return val_func
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# you called func(4, 4, 4)
# it returned 6

print()
print('   4. type_check')
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    # list_type = [str, int, float, complex, bool, tuple, list, set, dict]
    # if correct_type not in list_type:
    #     return f"Wrong type: {type(correct_type).__name__}. Was expected type: str, int, float, complex, bool, tuple, list, set, dict"
    # else:
        def checking_type(func):
            def inner(*args):
                list_type = [str, int, float, complex, bool, tuple, list, set, dict]
                if correct_type not in list_type:
                    print(f"Wrong type argument to decorator : {type(correct_type).__name__}. " \
                          f"Was expected type: str, int, float, complex, bool, tuple, list, set, dict")
                    return
                if type(*args) == correct_type:
                    return func(*args)
                else:
                    print(f"Wrong type input data for function - '{func.__name__}': {type(*args).__name__}. " \
                            f"Was expected: {correct_type.__name__}")
            return inner
        return checking_type


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number')) # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function