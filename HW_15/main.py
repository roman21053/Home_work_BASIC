# import sys
#
# def my_func():
#     message = sys.argv[1]
#     print(message)
#     print(sys.argv)
#
#
# if __name__ == "__main__":
#     my_func()

import argparse

def my_function():
    parser = argparse.ArgumentParser()
    parser.add_argument('number1', help="Enter first number for some action", type=int)
    parser.add_argument('number2', help="Enter second number for some action", type=int)
    parser.add_argument('action', help="Enter some action for numbers")
    args = parser.parse_args()
    if args.action == '+':
        print(args.number1 + args.number2)
    if args.action == '-':
        print(args.number1 - args.number2)
    if args.action == '*':
        print(args.number1 * args.number2)
    if args.action == '/':
        print(args.number1 / args.number2)


if __name__ == "__main__":
    my_function()
    print(5*4)