#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict_keys = sorted(a_dictionary)
    for key in sorted_dict_keys:
        print("{}: {}".format(key, a_dictionary[key]))
