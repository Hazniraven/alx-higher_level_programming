#!/usr/bin/python3
"""
    Write a class BaseGeometry based on 6-base_geometry
"""
class BaseGeometry:
    """
        class BaseGeometry with public instance method
        def area(self)
    """
    def area(self):
        """
            raises an Exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates the integer value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
