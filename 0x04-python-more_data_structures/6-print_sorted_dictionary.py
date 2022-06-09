#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    keys.sort()
    new_dict = {key: a_dictionary[key] for key in keys}
    for k, v in new_dict.items():
        print(f"{k}: {v}")
