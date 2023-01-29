#!/usr/bin/python3
'''defines a class square with a private instance attribute size
   with a setter and getter methods to retrieve and update the 
   attribute size, square has a public instance attribute size
   that gets the area of square'''
   

class Square:
    '''square with a PIA size'''

    def __init__(self, size=0):
        '''initializes self'''
        self.__size = size

    @property
    def size(self):
        '''gets the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size to value'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''gets the area of the square'''
        return self.__size * self.__size
