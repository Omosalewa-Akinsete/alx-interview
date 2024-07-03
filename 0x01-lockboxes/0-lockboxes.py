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

    n = len(boxes)
    visited = [False] * n

    # Mark the first box as visited
    visited[0] = True

    # Initialize a queue with the keys from the first box
    queue = boxes[0].copy()

    while queue:
        key = queue.pop(0)

        # If the key is valid (between 0 and n-1),
        # mark the corresponding box as visited
        if 0 <= key < n and not visited[key]:
            visited[key] = True

            # Add the keys from the newly visited box to the queue
            queue.extend(boxes[key])

    # Check if all boxes have been visited
    return all(visited)
