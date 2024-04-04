#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Function to determine if a given data set is a valid utf-8 encoding
    Args:
        data(list): data set containing multiple characters
    Return:
        boolean: true if data is valid utf-8 and false if otherwise
    """
    validutf8 = 0
    for value in data:
        byte = value & 255
        if validutf8:
            if byte >> 6 != 2:
                return False
            validutf8 -= 1
            continue
        while (1 << abs(7 - validutf8)) & byte:
            validutf8 += 1
        if validutf8 == 1 or validutf8 > 4:
            return False
        validutf8 = max(validutf8 - 1, 0)
    return validutf8 == 0
