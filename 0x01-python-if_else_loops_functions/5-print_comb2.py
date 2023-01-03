#!/usr/bin/python3
for num in range(0, 100):
    if num != 99:
        print('{0:02}, '.format(num), end="")
    else:
        print('{0:02}'.format(num), end="\n")
