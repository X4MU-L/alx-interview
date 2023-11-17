#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 5],
              [4, 5, 6, -1],
              [7, 8, 9, 3],
              [5, 9, 1, 25]]

    rotate_2d_matrix(matrix)
    print(matrix)

    
# 5, 7, 4, 1
# 9, 8, 5, 2
# 1, 9, 6, 3
# 25, 3, -1, 5