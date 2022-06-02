#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    arg_len = len(argv)

    if arg_len < 4:
        print("Usage: ./100-my_calculator.py < a > <operator > <b >")
        exit(1)

    arg1 = int(argv[1])
    operator = argv[2]
    arg2 = int(argv[3])

    if operator == "+":
        print("{} + {} = {}".format(arg1, arg2, add(arg1, arg2)))
    elif operator == "-":
        print("{} - {} = {}".format(arg1, arg2,  sub(arg1, arg2)))
    elif operator == "*":
        print("{} * {} = {}".format(arg1, arg2,  mul(arg1, arg2)))
    elif operator == "/":
        print("{} / {} = {}".format(arg1, arg2,  div(arg1, arg2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
