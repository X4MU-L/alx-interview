#!/usr/bin/python3

"""
create a pascal's triangle function
"""


def pascal_triangle(n):
    """returns an array of the pascal's triangle of n"""
    if n < 0:
        return []

    def factorial(x):
        """
            returns the factorial of x starting at 1
        """
        result = 1
        for n in range(1, x + 1):
            result *= n

        return result
    triangle = []
    for i in range(n):
        row = []
        for k in range(i + 1):
            pos = factorial(i) // (factorial(k) * factorial(i - k))
            row.append(pos)

        triangle.append(row)

    return triangle
