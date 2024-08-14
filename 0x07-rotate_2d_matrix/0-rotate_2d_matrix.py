#!/usr/bin/python3
"""Rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of lists): The 2D matrix to be rotated.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
