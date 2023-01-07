#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    length = len(argv)
    
    if length == 2:
        print("{} argument:".format(length - 1))
    elif length == 1:
        print("{} arguments.".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))

    for arg in argv:
        if i == 0:
            i += 1
            continue
        print("{}: {}".format(i, arg))
        i += 1
