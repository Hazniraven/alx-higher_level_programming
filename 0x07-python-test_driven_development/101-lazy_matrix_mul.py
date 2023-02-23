#!/usr/bin/python3
"""
    This module contains a function that uses the numpy
    module to multiply two matrices
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using the numpy module """

    matrix_mul = np.matmul(m_a, m_b).tolist()
    return matrix_mul
