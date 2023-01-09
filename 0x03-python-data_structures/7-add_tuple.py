#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2:
        first_ele_a = tuple_a[0]
        second_ele_a = tuple_a[1]
    elif len_a == 1:
        first_ele_a = tuple_a[0]
        second_ele_a = 0
    elif len_a == 0:
        first_ele_a = 0
        second_ele_a = 0

    if len_b >= 2:
        first_ele_b = tuple_b[0]
        second_ele_b = tuple_b[1]
    elif len_b == 1:
        first_ele_b = tuple_b[0]
        second_ele_b = 0
    elif len_b == 0:
        first_ele_b = 0
        second_ele_b = 0

    tuple_add = (first_ele_a + first_ele_b, second_ele_a + second_ele_b)
    return tuple_add
