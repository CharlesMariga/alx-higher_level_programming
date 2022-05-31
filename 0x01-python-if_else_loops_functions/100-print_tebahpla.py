#!/usr/bin/python3
for i in range(90, 64, -1):
    if (i % 2 == 0):
        # Print in lowercase
        print("{}".format(chr(i + 32)), end="")
    else:
        # Print in uppercase
        print("{}".format(chr(i)), end="")
