#!/usr/bin/python3
def islower(c):
    ascii_val = ord(c)
    if ascii_val > 96 and ascii_val < 123:
        return True
    else:
        return False
