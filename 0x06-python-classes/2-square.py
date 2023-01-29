#!/usr/bin/python3
'''Defines a square class with a private attribute size'''


class Square:
    '''class with a private attribute size'''

    def __init__(self, size=0):
        '''Initializes self'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
