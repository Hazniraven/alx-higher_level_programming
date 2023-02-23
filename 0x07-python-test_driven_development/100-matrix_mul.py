#!/usr/bin/python3
"""
    This module contains a function matrix_mul(a, b) that
    multiplies 2 matrices. if a or b is not a trix, a TypeError
    is raised.
"""


def matrix_mul(m_a, m_b):
    """ Multiplies a matrix """

    msg = ["m_a", "m_b"]
    matrixes = [m_a, m_b]
    for i in range(2):
        if type(matrixes[i]) is not list:
            raise TypeError("{} must be a list"
                            .format(msg[i]))

    for i in range(2):
        for li in matrixes[i]:
            if type(li) is not list:
                raise TypeError("{} must be a list of lists"
                                .format(msg[i]))

    for i in range(2):
        if len(matrixes[i]) == 0:
            raise ValueError("{} can't be empty".format(msg[i]))

    for li in matrixes[i]:
        if len(li) == 0:
            raise ValueError("{} can't be empty".format(msg[i]))

    for i in range(2):
        for li in matrixes[i]:
            for elem in li:
                if type(elem) is not int and type(elem) is not float:
                    raise TypeError("{} should contain only"
                                    " integers or floats"
                                    .format(msg[i]))

    for i in range(2):
        matrix = matrixes[i]
        row_size = len(matrix[0])
        for j in range(1, len(matrix)):
            if len(matrix[j]) != row_size:
                raise TypeError("each row of {} must be "
                                "of the same size"
                                .format(msg[i]))

    m_a_col_size = len(m_a[0])
    m_b_row_size = len(m_b)
    if m_a_col_size != m_b_row_size:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_mul = []
    for row in m_a:
	mat_row = []
        for j in range(len(m_b[0])):
            mul_sum = 0
            for i in range(m_a_col_size):
                mul_sum += row[i] * m_b[i][j]
            mat_row.append(mul_sum)
        matrix_mul.append(mat_row)

    return matrix_mul
