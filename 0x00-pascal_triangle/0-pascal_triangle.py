#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Return the list representing Pascal's triangle"""
    pas_list = []

    # Check if n is non-positive
    if n <= 0:
        return pas_list

    # Initialize the triangle with the first row
    pas_list.append([1])

    # Populate the rest of the triangle
    for i in range(n - 1):
        # Calculate each element in the current row
        current_row = ([1] + [pas_list[i][j] + pas_list[i][j + 1]
                       for j in range(len(pas_list[i]) - 1)] + [1])

        # Append the current row to the Pascal's triangle
        pas_list.append(current_row)

    return pas_list
