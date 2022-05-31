#!/usr/bin/python3
def print_last_digit(number):
    result = 0
    if number < 0:
        result = -number % 10
        print("{}".format(result), end="")
        return result
    else:
        result = number % 10
        print("{}".format(result), end="")
        return result
