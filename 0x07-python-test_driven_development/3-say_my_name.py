#!/usr/bin/python3
"""
    function that prints 'My name is <first name> <last name>'
    if first name and last name are not strings, raise a
    TypeError exception with the exception messaage 
    'first_name must be a string or last_name must be a string'
"""
def say_my_name(first_name, last_name=""):
    """ prints a name """
    if type(first_name) is not  str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
