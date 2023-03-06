#!/usr/bin/python3
"""
    This module contains a Rectangle class that inherits from
    superclass BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from class BaseGeometry """
    def __init__(self, width, height):
        """ Initializes self """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
