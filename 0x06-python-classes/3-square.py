#!/usr/bin/python3
'''defines a class Square with a private attribute size
   and a public attribute size to get the area of the
   square'''



class Square:
    '''class square with a private attribute size'''


    def __init__(self, size=0):
        '''initializes self'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''defines the area of square'''
        return self.__size * self.__size
