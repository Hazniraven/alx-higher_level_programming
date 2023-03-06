#!/usr/bin/python3
"""
    This module contains a function that adds an attribute to an object
"""

def add_attribute(obj, name, value):
    """ Adds an attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
