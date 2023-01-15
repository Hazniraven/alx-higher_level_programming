#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    dict_keys = list(a_dictionary)
    if len(dict_keys) == 0:
        return None
    else:
        biggest = a_dictionary[dict_keys[0]]
        name = dict_keys[0]
        for k, v in a_dictionary.items():
            if v > biggest:
                biggest = v
                name = k
        return name
