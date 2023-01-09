#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        column = len(row)
        for element in row:
            print("{:d}".format(element), end="")
            if column > 1:
                print(" ", end="")
                column -= 1
        print()
