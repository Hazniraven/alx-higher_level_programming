#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_del.append(key)
    for item in keys_to_del:
        del a_dictionary[item]
    return a_dictionary
