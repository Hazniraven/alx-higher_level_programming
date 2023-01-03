#!/usr/bin/python3
for alph_low in range(97, 123):
    if alph_low != 101 and alph_low != 113:
        print("{:c}".format(alph_low), end="")
