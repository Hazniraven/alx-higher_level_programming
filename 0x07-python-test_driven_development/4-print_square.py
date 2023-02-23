#!usr/bin/python3
"""
    A function that prints a square with the character
    # where size is the size length of the square. if size
    is not an integer, raise a TypeError exception message 
    'size must be an integer. if size < 0, a TypeError message
    is raised
"""
def print_square(size):
    """ prints a square with character # """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
	    print()
