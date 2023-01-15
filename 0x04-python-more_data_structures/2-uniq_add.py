#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    result = 0
    for number in uniq_list:
        result += number
    return result
