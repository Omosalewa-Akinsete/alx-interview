#!/usr/bin/python3
"""Maria and Ben playing a game"""


def primeNumbers(n):
    """
    Returns a list of prime numbers from start to end (inclusive)

    Args:
        start (int): Start number
        end (int): Last number to include
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines the winner of a prime numbers game

    Args:
        x (int): The number of rounds
        nums (list): An array

    Return:
        name of player who won the most rounds
        None, if the winner cannot be determined
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
