#!/usr/bin/python3
'''defines a class square with PIA size with a setter and getter
   methods and also with a public instance attribute area that
   gets the area of the square and print() that prints the square
   with character # to stdout'''


class Square:
    '''class square with a PIA size'''
    
    def __init_-(self, size=0):
        '''initializes self'''
        self.__size = size

    @property
    def size(self):
        '''returns the size of the square'''
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

    def my_print(self):
        '''prints the square with character # to stdout'''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
