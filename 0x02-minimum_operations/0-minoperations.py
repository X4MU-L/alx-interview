#!/usr/bin/python3

"""
    minimal operations
"""


def minOperations(n):
    """
    gets the minimal operations needed to get to a given
    number of characters
    args:
        n: number of characters
    """
    text = "H"

    lowest = num = n
    while True:
        result = tryOperations(n, num, text=text)
        num -= 1
        if num <= 0:
            break
        if result[0] <= lowest and len(result[1]) == n:
            lowest = result[0]

    return lowest


def copyOp(text):
    """return a char or string"""
    return text


def pasteOp(initialText, text):
    """return a string of cancatenated char to a string"""
    return initialText + text


def tryOperations(text_len, ops_range, text):
    """
        tryOperations - trys to copy and paste a string for a range
        returns number of minimal operations to get a given length

        args:
            text_len: length of string to arrive at
            ops_range: (int) how many times to try the operation
            text: (char) the given character to make up
            to a given length of characters

    """
    copy_pasted_text = text
    num_of_ops = 0

    for i in range(ops_range):
        if num_of_ops >= text_len or len(copy_pasted_text) == text_len:
            break
        copied_text = copyOp(copy_pasted_text)
        num_of_ops += 1

        for n in range(ops_range):
            if len(copy_pasted_text) == text_len:
                break
            copy_pasted_text = pasteOp(copied_text, copy_pasted_text)
            num_of_ops += 1

    return (num_of_ops, copy_pasted_text)
