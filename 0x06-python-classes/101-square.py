#!/usr/bin/python3
""" This module defines a square class with a private size attribute with
a setter and getter methods to retrieve and update the size attribute.
Square also has a public instance method area() that
gets the area of the square and
my_print() that prints the square with character # to stdout """


class Square:
    """ A square class with a private instance size attribute """
    
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes self """
        self.size = size
        self.position = position

    def __str__(self):
        s = ""
        if self.size == 0:
            return s
        for i in range(self.position[1]):
            s += "\n"
        for i in range(self.size):
            for k in range(self.position[0]):
                s += " "
            for j in range(self.size):
                s += "#"
            if i != self.size - 1:
                s += "\n"
        return s

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

    @property
    def position(self):
        """ Returns the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of the square to value """
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
        """ Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with character # to stdout """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
