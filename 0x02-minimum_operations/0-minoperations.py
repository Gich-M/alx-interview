#!/usr/bin/python3
"""Module for calculating the minimum number of operations
    required needed to reach n characters."""


def minOperations(n):
    """
    Calculate the minimum number of operations required to reach n characters.

    Args:
    n (int): The target number of characters.

    Returns:
        int: The minimum number of operations.
        0, if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

        if divisor * divisor > n:
            if n > 1:
                operations += n
            break

    return operations
