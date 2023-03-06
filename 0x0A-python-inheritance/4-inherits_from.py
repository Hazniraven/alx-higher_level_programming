#!/usr/bin/python3
"""
    write a function that returns True if the object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise false.
"""
def inherits_from(obj, a_class):
    """
        checks if the object inherits from the specified
	class
    """
    if type(obj) is a_class:
        return False
    return (isinstance(obj, a_class))
