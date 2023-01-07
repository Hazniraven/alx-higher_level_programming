#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    sum_ = 0
    if length > 1:
        for argc in range(1, length):
            sum_ += int(argv[argc])
    print(sum_)
