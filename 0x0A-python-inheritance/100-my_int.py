#!/usr/bin/python3
"""
    This module contains a class MyInt that inherits form the int class
    MyInt has == and != operators inverted
"""

class MyInt(int):
    """ MyInt class inherited from the class int """
    def __eq__(self, obj):
        """ Calls for equal to comparison """
        return super().__ne__(obj)
    
    def __ne__(self, obj):
        """ calls for not equal to comparison """
        return super().__eq__(obj)
