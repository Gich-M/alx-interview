#!/usr/bin/env python3
"""
Module to determine a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes.

    Return:
        bool: True if the data is valid UTF-8, else False.
    """
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if num_bytes > 0:
            if not (byte >> 6 == 0b10):
                return False
            num_bytes -= 1

        elif byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            num_bytes = 1

        elif byte >> 4 == 0b1110:
            num_bytes = 2

        elif byte >> 3 == 0b11110:
            num_bytes = 3

        else:
            return False
    return num_bytes == 0
