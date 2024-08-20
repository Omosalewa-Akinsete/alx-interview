#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be achieved with the coins.
    Returns:
    int: The fewest number of coins needed to meet total,
    or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the fewest coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
