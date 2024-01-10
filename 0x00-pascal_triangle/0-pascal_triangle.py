#!/usr/bin/env python3
"""Method that generates pascal triangle"""


def pascal_triangle(n):
    """Returns a list of list that forms a pascal triangle"""
    pascal_list = []

    if n <= 0:
        return pascal_list

    pascal_list.append([1])
    for i in range(n - 1):
        temp = [0] + pascal_list[-1] + [0]
        row = []
        for j in range(len(pascal_list[-1])+1):
            row.append(temp[j] + temp[j+1])
        pascal_list.append(row)
    return pascal_list
