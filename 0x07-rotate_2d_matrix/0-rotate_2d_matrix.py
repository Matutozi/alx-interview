#!/usr/bin/python3
"""This function rotate an n x n matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Function rotate an n x n matrix 90 degree clockwise"""

    # Transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
    return matrix
