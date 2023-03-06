#!/usr/bin/python3
"""
    This module contains a class Rectangle that inherits from 
    BaseGeometry (7-base_geometry.py).(task based on 
    8-rectangle.py)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle class that is a subclass of the BaseGeometry class """
    def __init__(self, width, height):
        """ Initializes self """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Function that makes the rectangle printable """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
  
    def area(self):
        """ implement the area() method """
        return (self.__width * self.__height)
