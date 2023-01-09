#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    list_len = len(my_list) - 1
    if idx > list_len:
        return None
    return my_list[idx]
