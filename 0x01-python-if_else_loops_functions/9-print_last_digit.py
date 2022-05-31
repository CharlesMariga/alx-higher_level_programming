def print_last_digit(number):
    result = 0
    if number < 0:
        result = -number % 10
        print("{}".format(result), end="")
        return -number % 10
    else:
        result = number % 10
        print("{}".format(result), end="")
        return -number % 10
