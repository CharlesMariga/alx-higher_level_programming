#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum = 0
    weight_count = 0
    for row in my_list:
        sum += row[0] * row[1]
        weight_count += row[1]
    return sum / weight_count
