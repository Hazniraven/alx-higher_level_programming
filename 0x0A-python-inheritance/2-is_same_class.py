#!/usr/bin/python3
"""
    This module contains a function that returns True
    if the object is exactly an instance of the specified
    class; otherwise False
"""
def is_same_class(obj, a_class):
    """
        returns True if the object is specified instance
	of a_class, or False if it is not.
    """
    return (type(obj) == a_class)
