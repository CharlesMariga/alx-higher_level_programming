#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for i in range(1, len(argv)):
        # print("This ran!")
        sum += int(argv[i])
    print(sum)
