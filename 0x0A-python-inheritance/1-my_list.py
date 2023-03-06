#!/usr/bin/python3
"""
    Write a class MyList that inherits from list
    and has a method print_sorted(self) that prints
    the list in a sorted manner.
"""
class MyList(list):
    """
       a class MyList that inherits from list
    """
    def print_sorted(self):
        """
            prints the list in a sorted manner
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
