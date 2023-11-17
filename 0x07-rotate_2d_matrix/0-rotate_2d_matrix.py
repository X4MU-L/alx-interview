#!/usr/bin/python3
"""
rotate a 2D array in place anticlockwise
"""


def rotate_2d_matrix(matrix):
    endStart = len(matrix[0]) - 1

    for _ in range(len(matrix[0]) // 2):
        for r in range(endStart, 0, -1):
            endStartNum = matrix[endStart - r][endStart]
            endEndNum = matrix[endStart][r]
            firstLast = matrix[r][endStart - endStart]
            matrix[endStart - r][endStart] =\
                matrix[endStart - endStart][endStart - r]
            matrix[endStart][r] = endStartNum
            matrix[r][endStart - endStart] = endEndNum
            matrix[endStart - endStart][endStart - r] = firstLast

        endStart -= 1
