#!/usr/bin/python3
"""
    Write a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size):
        """ Initializes self """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
