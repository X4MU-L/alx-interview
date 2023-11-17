#!/usr/bin/python3
"""
rotate a 2D array in place anticlockwise
"""


def rotate_2d_matrix(matrix):
    array_len = len(matrix)
    for layer in range(array_len // 2):
        first = layer
        last = array_len - 1 - layer
        for i in range(first, last):
            offset = i - first
            top_value = matrix[first][i]
            # swap the last with top
            matrix[first][i] = matrix[last - offset][first]
            # swap the bottom with last
            matrix[last - offset][first] = matrix[last][last - offset]
            # swap the right with bottom
            matrix[last][last - offset] = matrix[i][last]
            # swap the top with right
            matrix[i][last] = top_value
