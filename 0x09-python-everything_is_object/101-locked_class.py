#!/usr/bin/python3
"""
   This module contains a locked class that prevents the user
   from dynamically creating new instance attributes except if
   the attribute is first_name
"""


class LockedClass:
    """ A locked class """

    __slots__ = ["first_name"]

    def __init__(self):
        """ Initializes self """

        pass
