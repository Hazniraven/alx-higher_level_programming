#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for idx in range(0, x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, TypeError):
            pass
        else:
            n += 1
    print()
    return n
