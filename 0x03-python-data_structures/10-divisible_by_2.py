#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0 or my_list == None:
        return []
    return [i % 2 == 0 for i in range(len(my_list))]
