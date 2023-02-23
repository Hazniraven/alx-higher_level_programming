#!/usr/bin/python3
"""
    This module contains a function text_indentation(text)
    which prints a text with two newline after characters
    . ? or : if text is not a string, a TypeError is raised
"""


def text_indentation(text):
    """ Prints a text and two newlines after any of the
	characters . ? or 
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()
            print()
	    while (i + 1 != len(text) and text[i + 1] == " "):
                i += 1
        i += 1
