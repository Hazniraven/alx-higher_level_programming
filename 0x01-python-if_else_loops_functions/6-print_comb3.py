#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i == 8 and j == 9:
                print("89")
                break
            print("{}".format(i), end="")
            print("{}, ".format(j), end="")
