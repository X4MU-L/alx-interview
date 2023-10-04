#!/usr/bin/python3
"""
create a open box function
"""


def canUnlockAll(boxes):
    """
    the function checks if a box can be opened using the given
    conditions

        - boxes is a list of lists
        - A key with the same number as a box opens that box
        - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
        - The first box boxes[0] is unlocked
        - Return True if all boxes can be opened, else return False
    """

    opened_keys = {0}
    opened_boxes = {0}
    not_found = []
    for n in range(len(boxes)):
        if n in opened_keys:
            opened_boxes.add(n)
            opened_keys.update(boxes[n])
        else:
            not_found.append(n)

    for item in not_found:
        if item in opened_keys:
            opened_boxes.add(item)
            opened_keys.update(boxes[item])

    return len(boxes) == len(opened_boxes)
