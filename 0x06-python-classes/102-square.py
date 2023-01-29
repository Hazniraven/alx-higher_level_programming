#!/usr/bin/python3
""" This module defines a square class with a private size attribute with
a setter and getter methods to retrieve and update the size attribute.
Square also has a public instance method area() that
gets the area of the square """


class Square:
    """ A square class with a private instance size attribute """

    def __init__(self, size=0):
        """ Initializes self """
        self.__size = size

    def __eq__(self, other):
        """ Comparing instances """
        return self.area() == other.area()

    def __lt__(self, other):
        """ Comparing instances """
        return self.area() < other.area()

    def __le__(self, other):
        """ Comparing instances """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Comparing instances """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Comparing instances """
        return self.area() >= other.area()

    def __ne__(self, other):
        """ Comparing instances """
        return self.area() != other.area()

    @property
    def size(self):
        """ Returns the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size
