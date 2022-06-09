#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif1 = set_1 - set_2
    dif2 = set_2 - set_1
    return dif1.union(dif2)
