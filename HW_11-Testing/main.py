import unittest


def numbers(a: int) -> str:
    return {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}.get(a, "unexpected")


print(numbers(4))
