#!/usr/bin/python3
"""Module rotate_2d_matrix."""


def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.
    matrix - The input matrix to rotate.
    1. Transpose the matrix.
    2. Reverse each row.
    3. Swap elements from the start and end of the row.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], \
                matrix[i][j]
