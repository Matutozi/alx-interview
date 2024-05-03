#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Function that return the fewest number of operations needed to result in
    exactly n H characters in the file"""

    operation = 0
    min_operation = 2
    while n > 1:
        while n % min_operation == 0:
            operation += min_operation
            n = n / min_operation
        min_operation += 1
    return operation
