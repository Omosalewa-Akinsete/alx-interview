#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be achieved with the coins.

    Returns:
    int: The fewest number of coins needed to meet total,
    or -1 if it's not possible.
    """
    counted = tally = 0

    if total < 1:
        return 0

    for coin in sorted(coins)[::-1]:
        while counted + coin <= total:
            counted += coin
            tally += 1

    if counted != total:
        return -1

    return tally
