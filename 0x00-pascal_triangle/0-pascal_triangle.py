#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    n (int): The number of rows to generate.

    Return:
    list of lists: A list of lists of integers representing the
                    Pascal’s triangle of n.
                   An empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        new = [1]

        for j in range(1, i):
            new.append(prev[j - 1] + prev[j])

        new.append(1)
        triangle.append(new)

    return triangle
