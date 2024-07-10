#!/usr/bin/python3
"""
Method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return n

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
