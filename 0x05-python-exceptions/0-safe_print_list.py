#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for idx in range(0, x):
        try:
            print("{}".format(my_list[idx]), end="")
        except IndexError:
            pass
        else:
            n += 1
    print()
    return n
