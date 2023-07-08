#!/usr/bin/python3
"""Matrix multiplicatioin module"""


def matrix_mul(m_a, m_b):
    """"
    Multiplies two matrices

    Args:
        m_a: first matrix of type list of list of numbers
        m_b: second matrix of type list of list of numbers

    Raises:
        TypeError: if matrices are not of type list of list
        ValueError: if matrices are empty
        TypeError: if elements of matrices are not numbers
        ValueError: if matrices can not be multiplied

    Returns:
        A new matrix matrix which is a product of two matrices
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or float")
    for row in m_a:
        if len(m_a[0]) != len(row):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(m_b[0]) != len(row):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
