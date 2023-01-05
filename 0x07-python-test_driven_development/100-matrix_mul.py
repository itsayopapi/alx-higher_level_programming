#!/usr/bin/python3
"""Module to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """Function that multiplyes 2 matrices

    Args:

    m_a: matrix a
    m_b: matrix b

    -m_a and m_b must be a list of lists of ints or floats
    Else an error is raised
    """

    # Matrices must be lists

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Matrices must be list of lists

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(j, list) for j in m_b):
        raise TypeError("m_b must be a list of lists")

    # Matrices can't be empty

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    # All Elements of matrices must be ints or floats

    if not all([all(isinstance(j, (int, float)) for j in i) for i in m_a]):

        msg = "m_a should contain only integers or floats"
        raise TypeError(msg)

    if not all([all(isinstance(m, (int, float)) for m in k) for k in m_b]):

        msg = "m_b should contain only integers or floats"
        raise TypeError(msg)

    # Matrices must be square (all rows should be of the same size)

    checka = [len(i) for i in m_a]
    if len(set(checka)) != 1:
        msg = "each row of m_a must be of the same size"
        raise TypeError(msg)

    checkb = [len(j) for j in m_b]
    if len(set(checkb)) != 1:
        msg = "each row of m_b must be of the same size"
        raise TypeError(msg)

    # Matrices can only be multiplied if the number of columns
    # in m_a equals the number of rows in m_b

    if len(m_a[0]) != len(m_b):
        msg = "m_a and m_b can't be multiplied"
        raise ValueError(msg)

    # Multiplication

    res = []
    # Iteration of rows in m_a
    for i in range(len(m_a)):
        n_row = [sum([m_a[i][k] * m_b[k][j] for k in range(len(m_b))])
                 for j in range(len(m_b[0]))]
        res.append(n_row)

    return (res)
