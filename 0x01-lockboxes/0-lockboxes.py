#!/usr/bin/python3
"""
Defines a canUnlockAll function
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.
    Returns: True or False
    """
    keys = set()
    opened = set()
    not_opened = set()

    if not (isinstance(boxes, list) and
            all(isinstance(box, list) for box in boxes)):
        return False
    for i in range(len(boxes)):
        if i == 0:
            keys.update(boxes[i])
            opened.add(i)
        elif i in keys:
            keys.update(boxes[i])
            opened.add(i)
            for box in not_opened:
                if box in keys:
                    keys.update(boxes[box])
                    opened.add(box)
            not_opened.difference_update(opened)
        else:
            not_opened.add(i)

    if not_opened:
        return False
    return True