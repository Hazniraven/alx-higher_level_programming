#!/usr/bin/python3
"""
    This module contains a class Square that is inherited from the class
    Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """ a square class inherited from the rectangle class """
    def __init__(self, size):
        """ Initializes self """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Defines a __str__ function to print the square """
        return ("[Square] {}/{}".format(self.__size, self.__size))
