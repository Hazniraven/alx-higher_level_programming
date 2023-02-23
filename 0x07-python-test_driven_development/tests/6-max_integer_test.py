#!/usr/bin/python3
"""
    This Module contains a class to test the max_integer
    function
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ A class to test the max_integer function """

    def test_max_integer(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 6, 7]), 7)
        self.assertEqual(max_integer([-1, -200, 0, -150]), 0)
        self.assertEqual(max_integer([-1000, -100, -2, -5, -1]), -1)
        self.assertEqual(max_integer([10, 10, 10, 10, 10]), 10)
        self.assertEqual(max_integer([17, 2, 3, 5]), 17)
        self.assertEqual(max_integer([1]), 1)

        mat = [
            [1, 5, 7, 2],
            [0, 1, 17, -2],
            [1, 34, 17, 201],
            [-5, -200, 0, 0],
            [0.1, 0.2, 0.25, 0.5],
        ]

        for row in mat:
            self.assertEqual(max_integer(row), max(row))
