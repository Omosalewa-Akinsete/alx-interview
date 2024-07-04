#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
    boxes (list of lists): A list of lists,
    where each inner list represents the keys inside a box

    Returns:
    bool: True if all boxes can be opened, False otherwise
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
                keys.update(boxes[key])

    return all(unlocked)
