#!/usr/bin/python3
for i in range(90):
    if i % 10 != i // 10:
        if i == 89:
            print(i)
        elif i < ((i % 10) * 10 + i // 10):
            print("{:02d}".format(i), end=", ")
