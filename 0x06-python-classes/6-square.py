#!/usr/bin/python3
'''defines a square based on 5-square.py'''


class Square:
    '''class squar with PIA'''
    
    def __init__(self, size=0, position=(0, 0)):
        '''initializes self'''
        self.size = size
        self.position = position

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
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        '''gets the position of the square'''
        return self.__position
	
    @position.setter
    def position(self, value):
        '''sets the position of the square to value'''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
	
    def area(self):
        '''gets the area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''prints the square with character # to stdout'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
